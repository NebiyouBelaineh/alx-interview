#!/usr/bin/node
// script that prints all characters of a Star Wars movie depending on
// the movie id:
const request = require('request');
const movieId = process.argv[2];
const reqUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(reqUrl, async function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  const responseBody = JSON.parse(body);
  const characters = responseBody.characters;
  // Make a request for each character to get their name in an asynchronous way
  for (const element of characters) {
    try {
      const respChar = await new Promise(function (resolve, reject) {
        request(element, function (err, response, body) {
          if (err) {
            reject(err);
            return;
          }
          resolve(body);
        });
      });
      const resJson = JSON.parse(respChar);
      const name = resJson.name;
      console.log(name);
    } catch (error) {
      console.error(error);
    }
  }
});
