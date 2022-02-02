import { createClient } from 'redis';

const sub = createClient();

sub.on('error', (err) => {
  console.log('Redis client not connected to the server', err);
});

sub.on('connect', () => {
  console.log('Redis client connected to the server');
});

sub.subscribe('holberton school channel', () => {
});

sub.on('message', (ch, msg) => {
  if (msg === 'KILL_SERVER') {
    sub.unsubscribe();
    sub.quit();
  }
  console.log(msg);
});
