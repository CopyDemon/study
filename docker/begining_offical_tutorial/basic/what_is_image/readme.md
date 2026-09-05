# What is an image
A container image is a standardized package that includes all of the files, binaries, libraries, and configurations to run a container.  

For example:  
For a PostgreSQL image, that image will package the database binaries, config files, and other dependencies. For a Python web app, it'll include the Python runtime, your app code, and all of its dependencies.

## What we learned here
1. image is a template for creating containers it contains everything needed to run an application including code, runtime, system tools, system libraries, and settings etc.

1. image are immutable, we can only create new image or add changes on top of existing image.

        When an image exists (we call it **Base Image**) and we make changes to it, Docker won't directly modify the base image.  

        Instead, Docker creates a new **Layer** on top of the base image and applies changes only to that layer. (Think about **Photoshop layers**)

        **Lookup Logic**: Docker looks for files from the **Top Layer** (newest) down to the **Bottom Layer** (base). 
        - Once it finds the file in a layer, it **returns** that version and stops looking further down.
        - This "shadows" or "hides" the older versions of the file in the layers below.

        This is why we call images **immutable**: we never change the old layers; we only pile new layers on top.

    ```bash
    # Example: Top-Down Lookup

    [Layer 3] <delete file 1>  <- Docker finds "delete marker" here, stops, and tells you "file not found".
    [Layer 2] <add file 1>     <- This version is hidden (shadowed) by Layer 3.
    [Layer 1] <base image>     

    # In this example, File 1 is physically still inside Layer 2 (taking up disk space),
    # but logically it is "deleted" because Layer 3 says so.
    ```
