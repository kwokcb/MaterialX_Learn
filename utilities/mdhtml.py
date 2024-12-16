# Can also do this using:
# python -m markdown <file>.md -f <file>.html
import markdown
import sys, os, argparse, shutil

def convertToHtml(inputFileName, outputFileName, templateFileName=None, iframe=False, topFolder="..",
                  docFolder=".", footerFileName='footer.html', navFileName='navigation.html', removeMermaid=False):

    f = None
    html = ''
    htmlStyle = ''
    if not iframe:
        f = open(inputFileName, 'r', encoding="utf-8")
        text = f.read()
        if inputFileName.endswith('.md'):
            html = markdown.markdown(text, tab_length=2, extensions=['extra', 'md_in_html', 'codehilite', 'tables', 'toc'])
        else:
            html = ''
            # Read a line at a time from the html and print
            lineCount = 0
            inBody = False
            for line in text.splitlines():
                # if line starts with <!--Start--> then add the lines to html until <!--End--> is reached
                check = line.lstrip(' \t')
                if check.startswith('<!--Start-->'):
                    html = ''
                    inBody = True
                elif check.startswith('<!--End-->'):
                    inBody = False
                    break
                elif inBody:
                    # Split the line into words
                    words = line.split()
                    # Join the words back together with a space
                    new_line = ' '.join(words)
                    # Add the line back to the list with the original indentation
                    html += (line[:len(line) - len(line.lstrip())] + new_line) + '\n'

                    #html += '\t' + line + '\n'
                    lineCount += 1
            print('- Read %d body lines' % lineCount)

            htmlStyle = ''
            lineCount = 0
            inStyle = False
            for line in text.splitlines():
                # if line starts with <!--Start--> then add the lines to html until <!--End--> is reached
                check = line.lstrip(' \t')
                if check.startswith('<!--StyleStart-->'):
                    htmlStyle = ''
                    inStyle = True
                elif check.startswith('<!--StyleEnd-->'):
                    inStyle = False
                    break
                elif inStyle:
                    # Split the line into words
                    words = line.split()
                    # Join the words back together with a space
                    new_line = ' '.join(words)
                    # Add the line back to the list with the original indentation
                    htmlStyle += (line[:len(line) - len(line.lstrip())] + new_line) + '\n'

                    #html += '\t' + line + '\n'
                    lineCount += 1
            print('- Read %d style  lines' % lineCount)

        f.close()
    else:
        iframeString = '<iframe class="rounded" src="FILE_NAME" width="100%" height="800"></iframe>'
        html = iframeString.replace('FILE_NAME', os.path.basename(inputFileName))

    if templateFileName:
        footerText = ''
        if footerFileName:
            footer = open(footerFileName, 'r', encoding="utf-8")
            footerText = footer.read()

        navText = ''
        if navFileName:
            nav = open(navFileName, 'r', encoding="utf-8")
            navText = nav.read()

        t = open(templateFileName, 'r', encoding="utf-8")

        # Replace string in template with html
        template = t.read()
        html = template.replace('<!--FILL_CONTENT-->', html)
        html = html.replace('<!--Footer-->', footerText)
        html = html.replace('<!--Navigation-->', navText)        
        html = html.replace('<!--FILL_CONTENT_STYLE-->', htmlStyle)
        html = html.replace('_TOP_FOLDER_', topFolder)
        html = html.replace('_DOCUMENT_FOLDER_', docFolder)
        html = html.replace('“', "''")
        html = html.replace('”', "\"")
        html = html.replace('’', "'")
        html = html.replace('‘', "'")   
        html = html.replace('\u2318', "&#8984;")   

        if removeMermaid:
            html = html.replace('<script src="https://cdn.jsdelivr.net/npm/mermaid@9/dist/mermaid.min.js"></script>', '')
        t.close()

    outf = open(outputFileName, 'w')
    outf.write(html)
    outf.close()

def getOutputFileName(inputFileName, outputPath, inputExtension, outputExtension):
    if outputPath:
        return os.path.join(outputPath, os.path.basename(inputFileName).replace(inputExtension, outputExtension))
    else:
        return inputFileName.replace(inputExtension, outputExtension)    

def main():
    parser = argparse.ArgumentParser(description='Create a MaterialX document which references a set of images as pattern inputs.')
    parser.add_argument(dest='inputFileName', help='Root name of image files to examine.')
    # Add output path argument. Default to same directory as input file.
    parser.add_argument('-o', '--outputPath', dest='outputPath', help='Output path for the generated HTML file.')       
    # Add output filename argument. Default to same as input file.
    parser.add_argument('-of', '--outputFileName', dest='outputFileName', default="", help='Output filename for the generated HTML file.')       
    # Add input extension argument. Default to .md
    parser.add_argument('-e', '--extension', dest='extension', help='Input file extension to process. Default is .md', default='.md')
    # Add output extension argument. Default to .html
    parser.add_argument('-x', '--outputExtension', dest='outputExtension', help='Output file extension to process. Default is .html', default='.html')
    # Add template argument. Default to None
    parser.add_argument('-t', '--template', dest='template', help='Template file to use for generating the HTML file. Default is None', default=None)    
    # Add iframe argument. Default to False
    parser.add_argument('-i', '--iframe', dest='iframe', help='Use an iframe to display the input file. Default is False', action='store_true')
    # Add top folder
    parser.add_argument('-tp', '--top', dest='topfolder', default="..", help='Top folder. Default is ..')
    # Add doc folder
    parser.add_argument('-d', '--doc', dest='docfolder', default=".", help='Document foloder. Default is .' )
    parser.add_argument('-r', '--removeMermaid', dest='removeMermaid', type=bool, default=False, help='Remove Mermaid script from the HTML file. Default is False' )
    opts = parser.parse_args()

    extensionCheck = '.md'
    extensionCheck = '.html'
    outputExtension = opts.outputExtension
    if opts.iframe:
        opts.extension = '.html'
        outputExtension = '_iframe' + outputExtension
        print('Embedding as iframe')
        
    # If inputFileName is a directory, then process all .md files in the directory
    filePairs = []
    # Check if inputFileName is a directory
    if os.path.isdir(opts.inputFileName):
        for file in os.listdir(opts.inputFileName):
            if file.endswith(extensionCheck):
                inputFile = os.path.join(opts.inputFileName, file)
                inputFile = os.path.abspath(inputFile)

                # Copy input file to the path in opts.outputPath
                if opts.iframe:
                    outputFile = os.path.join(opts.outputPath, file)
                    print('- Copy %s to %s' % (inputFile, outputFile))
                    shutil.copyfile(inputFile, outputFile)

                outputFileName = getOutputFileName(inputFile, opts.outputPath, opts.extension, outputExtension)
                # Get absolute path to input file
                outputFileName = os.path.abspath(outputFileName)
                print('Convert pair: %s, %s' % (inputFile, outputFileName))
                filePairs.append((inputFile, outputFileName))
    else:
        inputFileName = opts.inputFileName
        # Copy input file to the path in opts.outputPath
        if opts.iframe:
            inputFileName = os.path.join(opts.outputPath, os.path.basename(opts.inputFileName))
            print('- Copy %s to %s' % (opts.inputFileName, inputFileName))
            shutil.copyfile(opts.inputFileName, inputFileName)
            inputFileName = os.path.basename(inputFileName)

        if (len(opts.outputFileName) > 0):
            outputFileName = getOutputFileName(opts.outputFileName, opts.outputPath, opts.extension, outputExtension)
        else:
            outputFileName = getOutputFileName(inputFileName, opts.outputPath, opts.extension, outputExtension)
        print('Convert pair: %s, %s' % (inputFileName, outputFileName))
        filePairs.append((inputFileName, outputFileName))

    for filePair in filePairs:
        print('- Convert %s to %s' % (filePair[0], filePair[1]))
        convertToHtml(filePair[0], filePair[1], opts.template, opts.iframe, opts.topfolder, opts.docfolder, 'footer.html',
                      'navigation.html',  opts.removeMermaid)

if __name__ == '__main__':
    main()

