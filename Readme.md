### Prerequisites
1. Python 3.9
2. Docker
3. pipenv

### Installation Guideline
1. Install necessary packages for development purposes locally using pipenv
   ```sh
    pipenv shell
    pipenv install --dev
   ```
2. Install pre-commit and commit-linter
   ```sh
   pre-commit install
   commit-linter install
   ```
3. Create a `.env` file by duplicating `.env.example`. Put the values according to your system setup.

4. Run Docker environment
    ```sh
    docker compose up --build
    ```
    Note: The `--build` is only need when you make  any dependencies changes in the project.
