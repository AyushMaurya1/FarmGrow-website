'use strict';

const express = require('express')
const path = require('path')
// const bcrypt = require('bcrypt')
// const collection = require('./config')
const PORT = 3000;

const app = express();

app.use(express.static(path.join(__dirname,"public")));

app.post("/api/register", async (req,res) => {
  const data = {
      username: req.body.username,
      email: req.body.email,
      password: req.body.password
  }

  // checking for existing user
  const existingUser = await collection.findOne({username: data.username});


  if(existingUser) {
      res.send("User already exist Try a different user name")
  }else {
      // hashing password
      const saltRounds = 10;
      const hashedPassword = await bcrypt.hash(data.password, saltRounds);

      // replace the hashed password
      data.password = hashedPassword;

      const userdata = await collection.insertMany(data);
      console.log(userdata);
  }

});

app.listen(PORT, ()=> {
  console.log(`Server is running on 
                  http://localhost:${PORT}`)
})

/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
}



/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const navLinks = document.querySelectorAll("[data-nav-link]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
}

addEventOnElem(navTogglers, "click", toggleNavbar);

const closeNavbar = function () {
  navbar.classList.remove("active");
  overlay.classList.remove("active");
}

addEventOnElem(navLinks, "click", closeNavbar);



/**
 * header active when scroll down to 100px
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElem = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

addEventOnElem(window, "scroll", activeElem);