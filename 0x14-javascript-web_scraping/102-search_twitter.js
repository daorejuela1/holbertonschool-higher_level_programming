#!/usr/bin/node
const request = require('request');
const CONSUMER_KEY = 'b0OAJF6wTxThvyTEFIxFyykws';
const CONSUMER_SECRET = 'XR3nrUQTnXec0Tfhs5Wj1ovs1IVBrsm1nUTrnDt4B20WVNrpDq';
const SEARCH_STRING = '#cisfun';
const oauth =
    {
      consumer_key: CONSUMER_KEY,
      consumer_secret: CONSUMER_SECRET
    };
const query = { q: SEARCH_STRING };
const AuthData = { grant_type: 'client_credentials' };
let url = 'https://api.twitter.com/oauth/request_token';
let i;
request.post({ url: url, auth: oauth, data: AuthData }, function (e, r, body) {
  url = 'https://api.twitter.com/1.1/search/tweets.json';
  request.get({ url: url, oauth: oauth, qs: query, json: true }, function (e, r, user) {
    for (i in user.statuses) {
      if (i === 5) { break; }
      const TweetID = user.statuses[i].id_str;
      const TweetText = user.statuses[i].text;
      const TweetOwner = user.statuses[i].user.name;
      console.log(`[${TweetID}] ${TweetText} by ${TweetOwner}`);
    }
  });
});
