## the problem which we have selected before mad2 project is grocery store

* is very import to think first that how you are gonna start or gonna work on a project where you have it's problem statement ;; which thing you will use 

* flask for api
* vueJs for ui
* Vue js advance with CLI
* bootstrap
* sqlite database
* Redis for caching
* it should be possible to run all the demos on the student's computer , which should be either be a linux based sys or should be able to simulate teh same . you can use wsl for windows os

## will see vue 3 set-up and vue cli set-up

* setup the backend (have seen in mad1 as it is)

## first -> Install Node.js properly inside WSL (BEST FIX)
* 1. Remove Windows Node usage from WSL -> `hash -r`
* 2. Install Node using nvm (recommended) -> `curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`

* 3. Restart terminal or run: -> `source ~/.bashrc`
* 4. Install a stable Node version (Vue CLI works best with LTS): -> `nvm install 18` , `nvm use 18`

* 5. `node -v`, `npm -v`, `which node`

* 6. Reinstall Vue CLI inside WSL -> `npm uninstall -g @vue/cli` and `npm install -g @vue/cli`, `vue create .` # . means create vue app in current folder

* now go to frontend -> and try to do it by using CLI method
-> `npm install -g @vue/cli`
-> `vue create .` # . means create vue app in current folder

* after that it will take some time and will be created important files for us ;; and these files are import for our frontend configration ;; it gives a base for what we need to be done in frontend

* so we need to modify this for interect with backend

* it has told that what things we have to install -> `npm install` -> (it will install all the dependencies) ;; after -> now want to start/run frontend give -> `npm run serve`


## there are two apis -> compositions api and optional apis

* so syntex will be change -> in optional api we use something like
* {
  data(){
    return {
      products:[]
    }
  },
  methods: {

  }
}


* and compositional apis we have like 
```<script setup>
  import {ref, onMounted} from 'vue'
  const product= ref()

  const getProduct = ()=>{
  fetch("http://127.0.0.1:5000/product")
  .then(res => res.json())
  .then(data =>{
    product.value= data
  })
  }

  onMounted(()=>{
    getProduct()
  })
  
</script>```