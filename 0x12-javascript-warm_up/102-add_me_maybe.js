#!/usr/bin/node
//Write a function that increments and calls a function.
function callMeMoby (number, theFunction) 
{
    theFunction(number + 1);
  }
  exports.callMeMoby = callMeMoby;
