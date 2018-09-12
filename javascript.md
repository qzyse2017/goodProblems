# JavaScript
_problems I overcame while using javascript_

## Loop through an array in JavaScript

1. use like below

```javascript
var myStringArray = ["Hello","World"];
var arrayLength = myStringArray.length;
for (var i = 0; i < arrayLength; i++) {
    alert(myStringArray[i]);
    //Do something
}
```

2. use `forEach`, not recommended to some extend, it is just supported by those compatible ES6.
you may see a example from mdn link below

3. not recommended -- `for .. in..`
It is for enumerate object properties

>zipcodeman suggests the use of the for...in statement, but for iterating arrays for-in should be avoided, that statement is meant to enumerate object properties.

>It shouldn't be used for array-like objects because:

>The order of iteration is not guaranteed, the array indexes may not be visited in numeric order.
Inherited properties are also enumerated.

>The second point is that it can give you a lot of problems, for example, if you extend the Array.prototype object to include a method there, that property will be also enumerated.

REF

https://stackoverflow.com/a/3010848/7122122

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


## How do I update Node.js?
```For Ubuntu:
sudo apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
sudo apt-get install -y nodejs
```

```
Use NVM(Node Version Manager)
https://github.com/creationix/nvm
```

REF:  
[answer from Stackoverflow](https://stackoverflow.com/questions/8191459/how-do-i-update-node-js)
