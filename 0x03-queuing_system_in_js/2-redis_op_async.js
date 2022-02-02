import { createClient } from 'redis';

import { promisify } from 'util';

const redis = require('redis');

const client = createClient();

promisify(client.get).bind(client);

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

let displaySchoolValue = async (schoolName) => {
  await client.get(schoolName, (err, value) => {
    if (err) throw err;
    console.log(value);
  });
};

displaySchoolValue = promisify(displaySchoolValue);

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
