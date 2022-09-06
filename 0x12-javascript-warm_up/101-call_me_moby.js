#!/usr/bin/node
exports.callMeMoby = function (x, theFuction) {
  while (x > 0) {
    theFuction();
    x--;
  }
};
