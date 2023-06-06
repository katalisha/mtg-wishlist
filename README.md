# Usage
`poetry run python src/main.py wishlist.csv`

# Running tests
`poetry run pytest`

# To run the environment
1. Download [Docker desktop](https://www.docker.com/products/docker-desktop/)
2. Download [vscode](https://code.visualstudio.com)
3. Install the [dev containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) to vscode
4. Click the remote link icon in the bottom left corner of vscode or use the command palette to 'Reopen in container'
5. Once everything has loaded you should be able to run app.py in vscode to see the current version of python is 3.11
You can now edit your files and run them in the container, they are still saved locally so you won't lose any edits if you kill the container.

Note: if the python extension isn't detected in vscode, you may need to reload the window once the container is running. You can do this in the command palette.

## Learn more about dev containers
- https://code.visualstudio.com/learn/develop-cloud/containers
- https://code.visualstudio.com/docs/devcontainers/create-dev-container

## Dragon shield app wishlist format
Quantity,Card Name,Set Code,Set Name,Card Number,Condition,Printing,Language,LOW,MID,MARKET
1,"Ao, the Dawn Sky",NEO,Kamigawa: Neon Dynasty,406,NearMint,Normal,English,3.20,5.20,5.02
1,Golgari Guildgate,GRN,Guilds of Ravnica,248,NearMint,Foil,English,0.44,0.60,0.62
