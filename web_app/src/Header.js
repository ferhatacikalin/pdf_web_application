import React from "react";
import axios from "axios";
export default class Header extends React.Component{
 constructor(props){
   super();
   this.state={
     show:false,
     username:null,
     is_admin:false,
     id:null
   }
  this.props=props;
 this.loadUser = this.loadUser.bind(this);
 }
 componentDidMount(){
  if(window.location.pathname !== '/login'){
    this.loadUser()
  }
  else{
    if(localStorage.getItem('access_token')){
      window.location='/'
    }
  }
 }
 loadUser(){
  var config = {
    method: 'get',
    url: 'http://localhost:8080/api/v1/me',
    headers: { 
      'Authorization': 'Bearer ' +  localStorage.getItem('access_token'),
    }
  };
  
  axios(config)
  .then( (response) => {
    if(response.status === 200){
        this.setState({username:response.data.username });
        this.setState({is_admin:response.data.is_admin });
        this.setState({id:response.data.id});
    }
    else{ window.location = '/login'}
  })
  .catch(function (error) {
    window.location = '/login'
  });
  
 }
 render( ){return (
    <div hidden={window.location.pathname === '/login'}>
      <nav class="bg-white dark:bg-gray-800  shadow ">
        <div class="max-w-7xl mx-auto px-8">
          <div class="flex items-center justify-between h-16">
            <div class="w-full justify-between flex items-center">
              <a class="flex-shrink-0" href="/">
                <a class=" font-extrabold" href="/#">
                  {this.state.username}
                </a>
                {/* <img class="h-8 w-8" src="/icons/rocket.svg" alt="Workflow"/> */}
              </a>
              <div class="hidden md:block">
                <div class="ml-10 flex items-baseline space-x-4">
                  <a
                    class="text-black-300  hover:text-gray-800 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    href="/upload_pdf"
                  >
                    Yükle
                  </a>
                  <a
                    class="text-black-300  hover:text-gray-800 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    href="/#"
                  >
                    Ara
                  </a>
                  <a
                    class="text-black-300  hover:text-gray-800 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    href="/project_list"
                  >
                    Tezler
                  </a>
                  <a
                  hidden={this.state.is_admin===false}
                    class="text-black-300  hover:text-gray-800 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    href="/project_list"
                  >
                    Kullanıcılar
                  </a>
                  <button
                  onClick={()=>{localStorage.removeItem('access_token');window.location='/login'}}
                    class="text-red-800  hover:text-gray-800 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    href="/project_list"
                  >
                   Çıkış Yap
                  </button>
                </div>
              </div>
            </div>
            <div class="block">
              <div class="ml-4 flex items-center md:ml-6"></div>
            </div>
            <div class="-mr-2 flex md:hidden">
              <button class="text-gray-800 dark:text-white hover:text-gray-300 inline-flex items-center justify-center p-2 rounded-md focus:outline-none">
                <svg
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="h-8 w-8"
                  viewBox="0 0 1792 1792"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path d="M1664 1344v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45z"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>

      </nav>
    </div>
 );}
}
