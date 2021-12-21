import axios from "axios";
import React from "react";

export default function ViewProject(){
    function editUser(id){
        window.location="/edit_user/"+id;
    }
    const [users, setUsers] = React.useState([]);
    var config = {
        method: 'get',
        url: "http://localhost:8080/api/v1/user/list",
        headers: { 
          'Authorization': 'Bearer '+localStorage.getItem('access_token'),
        }
      };
      
      axios(config)
      .then(function (response) {
        setUsers(response.data)
      })
      .catch(function (error) {
        console.log(error);
      });
      const items = users.map((user) =>
        <li className="flex flex-row">
        <div className="select-none cursor-pointer flex flex-1 items-center p-4">

            <div className="flex-1 pl-1 mr-16">
                <div className="font-medium dark:text-white">
                {user.id}
                </div>
                <div className="text-gray-600 dark:text-gray-200 text-sm">
                    {user.username}
                </div>
            </div>
            <div className="text-gray-600 dark:text-gray-200 text-xs">
                {user.is_admin ? 'Admin': 'Kullanıcı'}
            </div>
            <button  onClick={()=> editUser(user.id)} className="w-24 text-right flex justify-end">
                <svg width="20" fill="currentColor" height="20" className="hover:text-gray-800 dark:hover:text-white dark:text-gray-200 text-gray-500" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1363 877l-742 742q-19 19-45 19t-45-19l-166-166q-19-19-19-45t19-45l531-531-531-531q-19-19-19-45t19-45l166-166q19-19 45-19t45 19l742 742q19 19 19 45t-19 45z">
                    </path>
                </svg>
            </button>
        </div>
    </li>
      
      )
    return(
        <div>
       
        <div className="bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
           
<div className="container flex flex-col mx-auto w-full items-center justify-center bg-white dark:bg-gray-800 rounded-lg shadow">
    <div className="px-4 py-5 sm:px-6 border-b w-full">
        <h3 className="text-lg leading-6 font-medium text-gray-900 dark:text-white">
            Kullanıcılar
        </h3>
        <p className="mt-1 max-w-2xl text-sm text-gray-500 dark:text-gray-200">
            Kayıtlı Kullanıcılar
        </p>
    </div>
    <ul className="flex flex-col  w-9/12 -mx-1 divide divide-y ">

{items}

    </ul>
</div>

        </div>
        </div>
        )
}