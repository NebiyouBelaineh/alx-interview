#!/usr/bin/node

const request = require("request");
if (process.argv.length < 3) {
    // console.log("Usage ./0-starwars_characters.js <episode_id>");
    return
}
const film = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/" + film;


function requestPromise(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                resolve({ response, body });
            }
        });
    });
}

async function getCharacters() {
    try {
        const response = await requestPromise(url);
        const characters = JSON.parse(response.body).characters

        for (const character of characters) {
            try {
                const characterResponse = await requestPromise(character);
                console.log(JSON.parse(characterResponse.body).name);
            } catch (error) {
                console.error(error);
            }
        }
    }
    catch (error) {
        console.log(error)
    }
}

getCharacters();
