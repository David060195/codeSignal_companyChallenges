solution = (inputString, width) => {
  let window = "";
  let start = 0;
  let res = "";
  for (let end = 0; end < inputString.length; end++) {
    while (end - start > width) {
      start++;
    }
    window = inputString.substring(start, end);
    let word = inputString[end];
    let lenWord = 0;
    let foundIndex = -1;
    for (; ; lenWord++) {
      let index = window.indexOf(word);
      if (index === -1) break;
      word += inputString[end + lenWord + 1];
      foundIndex = index;
    }
    if (foundIndex >= 0) {
      res += `(${foundIndex + start},${lenWord})`;
      end += lenWord - 1;
    } else {
      res += inputString[end];
    }
  }
  return res;
};
