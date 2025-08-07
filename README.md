This is an app for automating the task of searching stores for hard to find Magic the Gathering cards (and also the project I am using to learn python).
It is a cli program that takes an exported [dragonshield](https://mtg.dragonshield.com) wishlist and a list of stores and searches each store for the wishlist cards.
It runs in a dev container but now it's probably easier to run locally using poetry.

# Usage
`poetry run python src/main.py -w wishlist.csv -s stores.csv -f hard-to-find.csv -v`

# Running tests
`poetry run pytest`
`poetry run pytest --cov=src`

# Running linter
`poetry run pylint --recursive=y src`

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

## store csv format
Currenlty only stores using binderpos are supported
Name,URL
"Tabernacle","https://tabernacle-games.myshopify.com"
"Plenty of Games","https://plenty-of-games-au.myshopify.com"
"Good Games","https://good-games-townhall.myshopify.com"
"MTG Mate","https://www.mtgmate.com.au"
"Cherry Collectables","https://kq0hnn.a.searchspring.io"

## hard to find csv format
Will highlight hard to find cards in the results, copy lines from wishlist
Quantity,Card Name,Set Code,Set Name,Card Number,Condition,Printing,Language,LOW,MID,MARKET
1,"Ao, the Dawn Sky",NEO,Kamigawa: Neon Dynasty,406,NearMint,Normal,English,3.20,5.20,5.02
1,Golgari Guildgate,GRN,Guilds of Ravnica,248,NearMint,Foil,English,0.44,0.60,0.62