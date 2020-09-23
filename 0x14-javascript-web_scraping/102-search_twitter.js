#!/usr/bin/node
const request = require('request');
const CONSUMER_KEY = process.argv[2];
const CONSUMER_SECRET = process.argv[3];
const SEARCH_STRING = process.argv[4];
const oauth =
    {
      consumer_key: CONSUMER_KEY,
      consumer_secret: CONSUMER_SECRET
    };
const query = {
  q: SEARCH_STRING,
  count: 5
};
const AuthData = { grant_type: 'client_credentials' };
let url = 'https://api.twitter.com/oauth/request_token';
request.post({ url: url, auth: oauth, data: AuthData }, function (e, r, body) {
  url = 'https://api.twitter.com/1.1/search/tweets.json';
  request.get({ url: url, oauth: oauth, qs: query, json: true }, function (e, r, users) {
    for (const user of users.statuses) {
      const TweetID = user.id_str;
      const TweetText = user.text;
      const TweetOwner = user.user.name;
      console.log(`[${TweetID}] ${TweetText} by ${TweetOwner}`);
    }
  });
});
