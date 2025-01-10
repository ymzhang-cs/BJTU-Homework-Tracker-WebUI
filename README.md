# BJTU-Homework-Tracker-WebUI

WebUI implement for [ymzhang-cs/BJTU-Homework-Tracker](https://github.com/ymzhang-cs/BJTU-Homework-Tracker).

## Dependencies

This project is written with JavaScript and Python, so you should download [Node.JS](https://nodejs.org/),
[pnpm](https://pnpm.io/) and [Python](https://www.python.org/).  
Then we can install the libraries we depend.  

1. Open a terminal with a working directory of the root of this repository

2. Install the dependencies for the main program
    ```shell
   pip install -r ./requirements.txt
    ```

3. Change directory to `web`.
    ```shell
   cd ./web
    ```

4. Install the dependencies for js
    ```shell
    pnpm install
    ```

## Run

1. [Install the dependencies](#Dependencies).

2. Build web ui.
    ```shell
   cd ./web
   pnpm build
    ```
   
    Every time you update the code under `web/`, you should run `pnpm build` to rebuild the web page.

3. Run the program
    ```shell
    python ./main.py
    ```
