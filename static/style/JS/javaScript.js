function clearAllFormInputs() {
    let form = document.getElementById('test123');
    let inputs = form.getElementsByTagName('span');
    for (let span of inputs)
      span.innerText = '';
  }
  let button = document.getElementById('button');
  button.addEventListener('click', clearAllFormInputs);
