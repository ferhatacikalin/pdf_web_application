import axios from "axios";
import React from "react";

export default class EditUser extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: null,
      username: null,
      is_admin: null,
      message:" "
    };

    this.componentDidMount = this.componentDidMount.bind(this);
    this.setUserName = this.setUserName.bind(this);
    this.setIsAdmin = this.setIsAdmin.bind(this);
    this.loadUser = this.loadUser.bind(this);
    this.editUser  =this.editUser.bind(this);
    this.deleteUser = this.deleteUser.bind(this);
  }
  setUserName(value) {
    this.setState({
      username: value,
    });
  }
  setIsAdmin(value) {
    this.setState({
      is_admin: value,
    });
  }
  editUser(){
      this.setState({message:" "});
    var FormData = require('form-data');
    var data = new FormData();
    data.append('username', this.state.username);
    
    data.append('is_admin', this.state.is_admin);
    
    var config = {
      method: 'post',
      url: 'http://localhost:8080/api/v1/user/update/'+this.state.id,
      headers: { 
        'Authorization': 'Bearer '+ localStorage.getItem('access_token') ,
        
      },
      data : data
    };
    
    axios(config)
    .then((response) => {
      if(response.status===200){
        this.setState({message:"Güncellendi"})  
      }
    })
    .catch(function (error) {
      console.log(error);
    });
    

  }
  deleteUser(){
    this.setState({message:" "});

    
    var config = {
      method: 'get',
      url: 'http://localhost:8080/api/v1/user/delete/'+this.state.id,
      headers: { 
        'Authorization': 'Bearer '+ localStorage.getItem('access_token') ,
        
      },
  
    };
    
    axios(config)
    .then((response) => {
      if(response.status===200){
        this.setState({message:"Silindi"})  
      }
    })
    .catch(function (error) {
      console.log(error);
    });
    
  }
  componentDidMount() {
    console.log(window.location.pathname.split("/")[2].toString());
    this.loadUser();
  }
  loadUser() {
    var config = {
      method: "get",
      url:
        "http://localhost:8080/api/v1/user/" +
        window.location.pathname.split("/")[2].toString(),
      headers: {
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    };

    axios(config)
      .then((response) => {
        this.setState(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  render() {
    return (
      <div>
        <div className="bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 sm:px-6">
            <h3 className="text-lg leading-6 font-medium text-gray-900">
              {this.state.username}
            </h3>
          </div>
          <div className="border-t border-gray-200">
            <dl>
              <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-lg font-medium text-gray-500">
                  Kullanıcı adı:
                </dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                  <input
                    value={this.state.username}
                    onChange={(event)=> this.setUserName(event.target.value) }
                    type="text"
                    className=" rounded-r-lg flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                  />
                </dd>
              </div>
              <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-lg font-medium text-gray-500">
                  Admin Yetkisi:
                </dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                  <select
                    value={this.state.is_admin === 'true' ? 'true' : 'false'}
                    onChange={(event)=>{this.setIsAdmin(event.target.value)}}
                    className=" rounded-r-lg flex-1  border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                  >
                    <option value="true"> Admin</option>
                    <option value="false">Kullanıcı</option>
                  </select>
                </dd>
                <div>

<button  onClick={this.editUser} type="button" className="py-2 px-4  bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-5/12 transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg ">
    Güncelle
</button>
<button  onClick={this.deleteUser} type="button" className="py-2 px-4  ml-5 bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-5/12 transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg ">
    Sil
</button>
<p className="w-10/12">{this.state.message}</p>
                  
                </div>
              </div>
            </dl>
          </div>
        </div>
      </div>
    );
  }
}
