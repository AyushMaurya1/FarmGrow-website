const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});



const form=document.getElementById('sign-up-form')
form.addEventListener('submit',registerUser);

async function registerUser(event) {
  event.preventDefault()
  const uname= document.getElementById('uname').value
  const email= document.getElementById('email').value
  const pass= document.getElementById('pass').value
  const re_pass= document.getElementById('re_pass').value
  const contact_number= document.getElementById('contact_number').value

  const result = await fetch('/api/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      uname,
      email,
      pass,
      re_pass,
      contact_number
    })
  }).then((res) => res.json())

  console.log(result)
}
