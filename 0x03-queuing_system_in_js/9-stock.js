import { createClient } from 'redis';

const express = require('express');

const app = express();
const port = 1245;

const util = require('util');
const redis = require('redis');

const client = createClient();
const hget = util.promisify(client.hget).bind(client);

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 250,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 450,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 4,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

function getItemById(id, listProducts) {
  for (let i = 0; i < Object.keys(listProducts).length; i += 1) {
    if (listProducts[i].id === parseInt(id, 10)) {
      return listProducts[i];
    }
  }
  return {};
}

function reserveStockById(itemId, stock) {
  client.hset('stock', `item.${itemId}`, JSON.stringify(stock), redis.print);
}

const getCurrentReservedStockById = async (itemId) => await hget('stock', `item.${itemId}`);

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  getCurrentReservedStockById(req.params.itemId)
    .then((item) => {
      if (item !== null) res.json(JSON.parse(item));
      else res.json({ status: 'Product not found' });
    }).catch((err) => {
      console.log(err);
    });
});

app.get('/reserve_product/:itemId', (req, res) => {
  const id = req.params.itemId;
  const item = getItemById(id, listProducts);
  if (Object.keys(item).length !== 0) {
    if (item.stock > 0) {
      reserveStockById(id, item);
      res.json({ status: 'Reservation confirmed', itemId: id });
    } else res.json({ status: 'Not enough stock available', itemId: id });
  } else res.json({ status: 'Product not found' });
});

app.listen(port, () => {
});
