# Case Study : Feature Extensions For MaterialX

This document outlines the history and approach taken to add a feature extension to MaterialX.

In this particular case it was to extend glTF support to support interchange to / from glTF to MaterialX.

# Repository Approaches

The following approaches were considered.

1. Directly as part of MaterialX core distribution.

   This has the immediate advantage of being part of all official releases but the greater advantage is the development infrastructure already exists and only needs to be extended.
   
   This includes:
    * testing frameworks, 
    * language wrappers for Python, Javascript, etc 
    * documentation
    * CI / CD
    * Static analysis for code quality.

   One main question to ask and have discussed is whether the new feature / extension belongs as part of "core". Some repositories include extensions as part of the core repo and some do not.

   If core acceptance is not possible then other options need to be considered.

2. Custom MaterialX distribution.

   For this we will consider a "fork" of the main 
   repository. 

   If all of the infrastructure is executed to 
   keep in sync with the standards of the core repo
   then injecting additional support for the feature / extension can be performed. There is however the maintenance cost of keeping in sync
   in case any of the dependencies change.

   One natural down-side is adoption of this custom
   distribution and how to handle possible conflicting distributions between multiple feature extensions.

   This does not mean that while developing the feature / extension a fork is not recommended.

3. Custom feature distribution using 
   * A binary release of MaterialX
   * MaterialX as a build dependency.

   This option has the initial disadvantage of
   keeping in sync with the dependent distribution.

   Using an official release version also that any intermediate requirements or core enhancements cannot be taken into consideration. Also as the builds are pre-configured for a specific platform/target setup, either tha desired platform may not be available, or incompatible with the feature distribution deployment target.

   The alternative is to build the core distribution. One possibility is using a "submodule". If it's off of the core repo then this will help to stay in sync and still allow for usage of a non-released dependency. There is "grey" area that if a proposed core enhancement (PR) is
   not part of the core repo then a fork/branch becomes the
   dependent. 
   
   An alternative to "submodule" usage could be "subtree" usage. For this feature a "submodule" approach was taken along with branching for local core additions.

 # "Guiding Principles"

 The following are a set of "guiding principles" or just guidelines on how to write the extension / feature.

 As mentioned the best is to take what is already there and extend it. MaterialX is already broken down into "core" and "non-core" modules, so the first step is finding out where the feature should reside. The lower down in the dependency stack means the greater chance of side-effects thus ...




