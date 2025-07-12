class TreeVisualizer {
    /* A reusable D3 collapsible tree class that supports zooming, collapsing, and expanding nodes.
     * It can be instantiated with a container ID, SVG ID, zoom group ID, data, and optional colors for nodes.
     * The class provides methods to render the tree, collapse all nodes, expand all nodes, and fit the view.
     * @param {string} containerId - The ID of the container element for the tree.
     * @param {string} svgId - The ID of the SVG element where the tree will be drawn.
     * @param {string} zoomGroupId - The ID of the group element for zooming.
     * @param {Object} data - The hierarchical data to be visualized as a tree.
     * @param {Object} [options] - Optional settings for the tree, including colors for nodes.
     * @param {string} [options.collapsedColor] - Color for collapsed nodes (default: '#28a745').
     * @param {string} [options.expandedColor] - Color for expanded nodes (default: '#007bff').
     * @param {string} [options.leafColor] - Color for leaf nodes (default: '#ffffff').
     */
    constructor(containerId, svgId, zoomGroupId, data, options) {
        this.data = data;
        this.root = d3.hierarchy(data);
        this.container = document.getElementById(containerId);
        this.svg = d3.select(`#${svgId}`);
        this.zoomGroup = d3.select(`#${zoomGroupId}`);
        this.matches = [];
        this.currentHighlight = null;
        this.isVertical = false; // Default to horizontal layout

        this.nodeColors = options;

        // Initialize nodeClickAction as null
        this.nodeClickAction = null;

        this.zoom = d3.zoom()
            .scaleExtent([0.01, 20])
            .on('zoom', (event) => {
                this.zoomGroup.attr('transform', event.transform);
            });

        this.svg.call(this.zoom);
        this.initialize();
    }

    // Method to set the node click action
    setNodeClickAction(fn) {
        this.nodeClickAction = fn;
    }

    // Method to toggle orientation
    toggleOrientation() {
        this.isVertical = !this.isVertical;
        this.render();
        this.fitToView(false);
    } initialize() {
        this.root.children?.forEach(this.collapseAll);
        this.render();
        this.fitToView(true);
        this.updateNavigationButtons();
    }

    collapseAll(d) {
        if (d.children) {
            d._children = d.children;
            d._children.forEach(TreeVisualizer.prototype.collapseAll);
            d.children = null;
        }
    }

    expandAll(d) {
        if (d._children) {
            d.children = d._children;
            d._children = null;
        }
        if (d.children) {
            d.children.forEach(this.expandAll.bind(this));
        }
    }

    performExpandAll() {
        //this.currentHighlight = null;
        this.expandAll(this.root);
        this.render();
        this.fitToView(true);
    }

    performCollapseAll() {
        this.root.children?.forEach(this.collapseAll);
        this.render();
        this.fitToView(true);
        // TODO: Sometimes the bbox for the rects
        // are not computed properly.
    }

    clickAction(event, d) {
        // If click is not on a node (d is undefined/null), clear highlight and rerender
        if (!d) {
            //console.log('Click outside node, clearing highlight');
            if (this.currentHighlight) {
                this.currentHighlight = null;
                this.render();
            }
            // Call nodeClickAction with null to indicate no node was clicked
            if (typeof this.nodeClickAction === 'function') {
                this.nodeClickAction(null);
            }
            return;
        }
        let needUpdate = false;
        let needFit = false;
        if (d.children) {
            d._children = d.children;
            d.children = null;
            this.currentHighlight = d;
            needUpdate = true;
            needFit = true;
        } else if (d._children) {
            d.children = d._children;
            d._children = null;
            this.currentHighlight = d;
            needUpdate = true;
            needFit = true;
        }
        else {
            const path = d.ancestors().map(n => n.data.name).reverse().join('/');
            if (typeof this.nodeClickAction === 'function') {
                this.nodeClickAction(path);
            }
            this.currentHighlight = d;
            needUpdate = true;
        }
        //console.log('needUpdate', needUpdate, 'needFit', needFit);

        if (needUpdate) {
            this.render();
            this.updateNavigationButtons();
            if (needFit) {
                this.fitToView(false);
            }
        }
    }

    updateData(newData) {
        this.data = newData;
        this.root = d3.hierarchy(newData);
        this.initialize();
        this.clearHighlights();
    }

    updateChartColors(nodeColors) {
        this.nodeColors = nodeColors;
        //console.log("Updating chart colors...", this.nodeColors);
        this.render();
    }

    render() {
        this.zoomGroup.selectAll('*').remove();

        const treeLayout = d3.tree().nodeSize([this.isVertical ? 120 : 40, 1]);
        treeLayout(this.root);

        if (this.isVertical) {
            // Vertical layout: adjust spacing for vertical flow
            const VERTICAL_SPACING = 150;
            this.root.each(d => {
                // For vertical layout, depth determines y position, 
                // and x stays as calculated by d3.tree()
                d.y = d.depth * VERTICAL_SPACING;
                // d.x remains as calculated by d3.tree() for horizontal spread
            });
        } else {
            // Horizontal layout (original)
            const HORIZONTAL_SPACING = 350;
            this.root.each(d => {
                d.y = d.depth * HORIZONTAL_SPACING;
            });
        }

        // Draw links
        this.zoomGroup.selectAll('.link')
            .data(this.root.links())
            .join('path')
            .attr('class', 'link')
            .attr('fill', 'none')
            .attr('stroke-width', '0.5px')
            .attr('stroke', this.nodeColors.linkColor)
            .attr('d', this.isVertical ?
                d3.linkVertical().x(d => d.x).y(d => d.y) :
                d3.linkHorizontal().x(d => d.y).y(d => d.x)
            );

        // Draw nodes
        const node = this.zoomGroup.selectAll('.node')
            .data(this.root.descendants())
            .join('g')
            .attr('class', 'node')
            .attr('transform', d => this.isVertical ?
                `translate(${d.x},${d.y})` :
                `translate(${d.y},${d.x})`
            );

        // Create a circle for current highlighted node
        node.append('circle')
            .attr('r', 20)
            .attr('cx', 0)
            .attr('cy', 0)
            .attr('class', 'node-circle')
            .style('fill', 'transparent')
            .style('stroke-width', d => (this.currentHighlight === d) ? '2px' : '0px')
            .style('stroke', d => (this.currentHighlight === d ? '#2d96f2' : 'transparent'));

        // Clickable large transparent background circle (for click + hover)
        const hoverColor = this.nodeColors.hoverColor;
        node.append('circle')
            .attr('r', 20)
            .style('fill', 'transparent')
            .style('cursor', 'pointer')
            .on('click', (event, d) => {
                //console.log("Node clicked", d.data.name);
                this.clickAction(event, d);
            })
            .on('mouseover', (event) => d3.select(event.currentTarget).style('fill', hoverColor))
            .on('mouseout', (event) => d3.select(event.currentTarget).style('fill', 'transparent'));

        // Visual circle
        this.node_shape = 'circle';
        if (this.node_shape === 'circle') {
            node.append('circle')
                .attr('r', 5)
                .style('pointer-events', 'none')
                .attr('fill', d =>
                    d._children ? this.nodeColors.collapsedColor :
                        d.children ? this.nodeColors.expandedColor :
                            this.nodeColors.leafColor
                );
        }
        else {
            node.append('rect')
                .attr('width', 12)
                .attr('height', 12)
                .attr('x', -6)
                .attr('y', -6)
                .attr('class', 'node-rect')
                .style('pointer-events', 'none')
                .attr('fill', d =>
                    d._children ? this.nodeColors.collapsedColor :
                        d.children ? this.nodeColors.expandedColor :
                            this.nodeColors.leafColor
                );
        }

        // Labels (with clickable rect background)
        const labels = node.append('g')
            .attr('transform', d => {
                if (this.isVertical) {
                    // In vertical mode, all labels go below nodes
                    return 'translate(0,18)';
                } else {
                    // In horizontal mode, labels go left/right based on node type
                    return `translate(${d.children || d._children ? -12 : 12},0)`;
                }
            });

        const text = labels.append('text')
            .attr('fill', this.nodeColors.labelTextColor)
            .attr('text-anchor', d => {
                if (this.isVertical) {
                    return 'middle';
                } else {
                    return (d.children || d._children) ? 'end' : 'start';
                }
            })
            .attr('alignment-baseline', this.isVertical ? 'hanging' : 'middle')
            .attr('font-weight', d => (this.matches.includes(d) || this.currentHighlight === d) ? 'bold' : 'normal')
            .attr('font-size', '8px')
            .attr('font-family', 'sans-serif')
            .attr('pointer-events', 'none')
            .style('user-select', 'none')
            .style('cursor', 'default')
            .text(d => d.data.name);

        labels.append('rect')
            .lower() // Push rect behind text
            .attr('fill', this.nodeColors.labelBackgroundColor)
            .style('cursor', 'pointer')
            .style('stroke-width', d => (this.matches.includes(d) || this.currentHighlight === d) ? '2px' : '1px')
            .style('stroke', d => (this.matches.includes(d) ? this.nodeColors.highlightBorderColor : this.nodeColors.labelBorderColor))
            .on('click', (event, d) => {
                //console.log("Label clicked", d.data.name);
                this.clickAction(event, d);
            });

        // Set label rects to fit text size.
        labels.select('rect')
            .each(function (_, i) {
                const bbox = text.nodes()[i].getBBox();
                d3.select(this)
                    .attr('x', bbox.x - 2)
                    .attr('y', bbox.y - 2)
                    .attr('width', bbox.width + 4)
                    .attr('height', bbox.height + 4);
            });
    }

    resize() {
        this.render();
        this.fitToView(false);
    }

    fitToView(all = true) {
        //console.log("Fitting to view, all:", all);
        if (!all && this.currentHighlight) {
            //console.log('fit active highlight:', this.currentHighlight.data.name);
            this.highlightNode(this.currentHighlight);
            return;
        }

        //console.log('Fitting to view all nodes');

        const bounds = this.zoomGroup.node().getBBox();
        const fullWidth = this.container.clientWidth;
        const fullHeight = this.container.clientHeight;

        const scale = 0.95 / Math.max(bounds.width / fullWidth, bounds.height / fullHeight);
        const translateX = (fullWidth - bounds.width * scale) / 2 - bounds.x * scale;
        const translateY = (fullHeight - bounds.height * scale) / 2 - bounds.y * scale;

        this.svg.transition()
            .duration(500)
            .call(this.zoom.transform, d3.zoomIdentity.translate(translateX, translateY).scale(scale));
    }

    searchNodes(searchTerm, expandMatches = true) {
        try {
            const regex = new RegExp(searchTerm, 'i');
            this.matches = [];

            this.root.each(d => {
                if (regex.test(d.data.name)) {
                    this.matches.push(d);

                    if (expandMatches) {
                        let parent = d.parent;
                        while (parent) {
                            if (parent._children) {
                                parent.children = parent._children;
                                parent._children = null;
                            }
                            parent = parent.parent;
                        }
                    }
                }
            });

            this.render();

            if (this.matches.length > 0) {
                this.fitToMatches();
            }

            return this.matches;
        } catch (e) {
            console.error("Invalid regular expression:", e);
            return [];
        }
    }

    fitToMatches() {
        if (this.matches.length === 0) return;

        let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

        this.matches.forEach(match => {
            minX = Math.min(minX, match.x);
            minY = Math.min(minY, match.y);
            maxX = Math.max(maxX, match.x);
            maxY = Math.max(maxY, match.y);
        });

        const padding = 50;
        minX -= padding;
        minY -= padding;
        maxX += padding;
        maxY += padding;

        const containerWidth = this.container.clientWidth;
        const containerHeight = this.container.clientHeight;

        let width, height;

        if (this.isVertical) {
            width = maxX - minX;
            height = maxY - minY;
        } else {
            width = maxY - minY;
            height = maxX - minX;
        }

        const scale = Math.min(
            0.95 * containerWidth / width,
            0.95 * containerHeight / height
        );

        let translateX, translateY;

        if (this.isVertical) {
            translateX = (containerWidth - width * scale) / 2 - minX * scale;
            translateY = (containerHeight - height * scale) / 2 - minY * scale;
        } else {
            translateX = (containerWidth - width * scale) / 2 - minY * scale;
            translateY = (containerHeight - height * scale) / 2 - minX * scale;
        }

        this.svg.transition()
            .duration(500)
            .call(this.zoom.transform, d3.zoomIdentity.translate(translateX, translateY).scale(scale));
    }

    clearHighlights() {
        this.matches = [];
        this.currentHighlight = null;
        this.render();
        this.updateNavigationButtons();
        if (typeof this.nodeClickAction === 'function') {
            this.nodeClickAction(null);
        }
    }

    highlightNode(node) {
        // Expand all ancestors first
        let parent = node.parent;
        while (parent) {
            if (parent._children) {
                parent.children = parent._children;
                parent._children = null;
            }
            parent = parent.parent;
        }

        this.currentHighlight = node;

        const path = node.ancestors().map(n => n.data.name).reverse().join('/');
        if (typeof this.nodeClickAction === 'function') {
            this.nodeClickAction(path);
        }

        this.render();

        // Center view on this node
        const scale = 2.0;
        let translateX, translateY;

        if (this.isVertical) {
            translateX = (this.container.clientWidth / 2) - node.x * scale;
            translateY = (this.container.clientHeight / 2) - node.y * scale;
        } else {
            translateX = (this.container.clientWidth / 2) - node.y * scale;
            translateY = (this.container.clientHeight / 2) - node.x * scale;
        }

        this.svg.transition()
            .duration(300)
            .call(this.zoom.transform, d3.zoomIdentity.translate(translateX, translateY).scale(scale));

        // Update navigation button states
        this.updateNavigationButtons();
    }

    // Navigation methods for highlighted node
    navigateToParent() {
        if (!this.currentHighlight) return false;

        const parent = this.currentHighlight.parent;
        if (parent) {
            this.highlightNode(parent);
            return true;
        }
        return false;
    }

    navigateToFirstChild() {
        if (!this.currentHighlight) return false;

        // Check for visible children first
        if (this.currentHighlight.children && this.currentHighlight.children.length > 0) {
            this.highlightNode(this.currentHighlight.children[0]);
            return true;
        }

        // If no visible children but there are collapsed children, expand and navigate
        if (this.currentHighlight._children && this.currentHighlight._children.length > 0) {
            this.currentHighlight.children = this.currentHighlight._children;
            this.currentHighlight._children = null;
            this.render();
            this.highlightNode(this.currentHighlight.children[0]);
            return true;
        }

        return false;
    }

    navigateToNextSibling() {
        if (!this.currentHighlight || !this.currentHighlight.parent) return false;

        const siblings = this.currentHighlight.parent.children || [];
        const currentIndex = siblings.indexOf(this.currentHighlight);

        if (currentIndex !== -1 && currentIndex < siblings.length - 1) {
            this.highlightNode(siblings[currentIndex + 1]);
            return true;
        }

        return false;
    }

    navigateToPreviousSibling() {
        if (!this.currentHighlight || !this.currentHighlight.parent) return false;

        const siblings = this.currentHighlight.parent.children || [];
        const currentIndex = siblings.indexOf(this.currentHighlight);

        if (currentIndex > 0) {
            this.highlightNode(siblings[currentIndex - 1]);
            return true;
        }

        return false;
    }

    navigateToLastSibling() {
        if (!this.currentHighlight || !this.currentHighlight.parent) return false;

        const siblings = this.currentHighlight.parent.children || [];
        if (siblings.length > 0) {
            this.highlightNode(siblings[siblings.length - 1]);
            return true;
        }

        return false;
    }

    navigateToFirstSibling() {
        if (!this.currentHighlight || !this.currentHighlight.parent) return false;

        const siblings = this.currentHighlight.parent.children || [];
        if (siblings.length > 0) {
            this.highlightNode(siblings[0]);
            return true;
        }

        return false;
    }

    // Update navigation button states based on current highlight
    updateNavigationButtons() {
        const navParentBtn = document.getElementById('navParentBtn');
        const navPrevSiblingBtn = document.getElementById('navPrevSiblingBtn');
        const navNextSiblingBtn = document.getElementById('navNextSiblingBtn');
        const navChildBtn = document.getElementById('navChildBtn');

        if (!this.currentHighlight) {
            // Disable all navigation buttons when no node is highlighted
            navParentBtn.disabled = true;
            navPrevSiblingBtn.disabled = true;
            navNextSiblingBtn.disabled = true;
            navChildBtn.disabled = true;
            return;
        }

        // Enable/disable parent navigation
        navParentBtn.disabled = !this.currentHighlight.parent;

        // Enable/disable child navigation
        const hasChildren = (this.currentHighlight.children && this.currentHighlight.children.length > 0) ||
            (this.currentHighlight._children && this.currentHighlight._children.length > 0);
        navChildBtn.disabled = !hasChildren;

        // Enable/disable sibling navigation
        if (this.currentHighlight.parent) {
            const siblings = this.currentHighlight.parent.children || [];
            const currentIndex = siblings.indexOf(this.currentHighlight);

            navPrevSiblingBtn.disabled = currentIndex <= 0;
            navNextSiblingBtn.disabled = currentIndex >= siblings.length - 1;
        } else {
            navPrevSiblingBtn.disabled = true;
            navNextSiblingBtn.disabled = true;
        }
    }

    // Export functionality
    exportAsSVG() {
        const svgNode = this.svg.node();
        const serializer = new XMLSerializer();
        let svgString = serializer.serializeToString(svgNode);

        // Add XML declaration and DOCTYPE for better compatibility
        svgString = '<?xml version="1.0" encoding="UTF-8"?>\n' + svgString;

        const blob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'tree-visualization.svg';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }

    exportAsPNG() {
        const svgNode = this.svg.node();
        const svgData = new XMLSerializer().serializeToString(svgNode);

        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        const img = new Image();

        // Get SVG dimensions
        const rect = svgNode.getBoundingClientRect();
        canvas.width = rect.width * 2; // Higher resolution
        canvas.height = rect.height * 2;

        img.onload = function () {
            ctx.scale(2, 2); // Scale for higher resolution
            ctx.fillStyle = tree.nodeColors.labelBackgroundColor || 'white';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 0, 0);

            canvas.toBlob(function (blob) {
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.download = 'tree-visualization.png';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(url);
            });
        };

        const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
        const url = URL.createObjectURL(svgBlob);
        img.src = url;
    }
}
