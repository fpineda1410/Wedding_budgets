
import React from "react";
import { Redirect } from "react-router";



const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
            global_url:"https://3001-teal-moth-1dwi7eav.ws-us03.gitpod.io/",
			bearer_token: '',
			login: false,
            budget:[],
            services_data:[],
            freeAPIKey : '6eb74eb3f0325b10d40d',
            USD_api:'',
            CRC_api:'',
            USDvsCRC:'',
            //locations sorted data
            herradura_data:[],
            swiss_travel_data:[],
            sheraton_data:[],
            papagayo_data:[],
            //flowers sorted data
            flores_cr_data:[],
            flores_gala_data:[],
            flores_juno_data:[],
            flores_nandallo_data:[],
            //photographers sorted data
            gabriel_anta_data:[],
            douglas_cedeno_data:[],
            raw_shoots_data:[],
            geoff_photography_data:[],
            flower_indicator:'',
            location_indicator:'',
            photo_indicator:'',
            flower_provider:'',
            location_provider:'',
            photo_provider:'',
            update_budget_array:[0,0,0],
            recovery_redirect:false
        },
        
		actions: {

            deleteItem: element =>{
                console.log (element) //si es un hotel-flores... {category id}
                if (element.category=="Flowers"){
                    setStore({flower_indicator:''})
                    setStore({flower_provider:''})
                }
                if (element.category=="Location"){
                    setStore({location_indicator:''})
                    setStore({location_provider:''})
                }
                if (element.category=="Photography"){
                    setStore({photo_indicator:''})
                    setStore({photo_provider:''})
                }
            },
			login_user: async (username, password) => {
                let temp_token;
                let login_status;
                console.log(username,password);
				const store = getStore();
                
				const requestOptions = {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({ username: username, password: password })
				};

				const result =await fetch(store.global_url + "api/login", requestOptions)
					        .then(response => login_status=response.status)
                            .then(data =>  temp_token=data.access_token);
                console.log(temp_token);
                setStore({bearer_token:temp_token})

                if (response_status==200){
                    setStore ({login_redirect:true})
                }

				if (store.bearer_token.length > 0) {
					setStore({ login: true });
				}
				const requestOptions_budget = {
					method: "GET",
					headers: {
						"Content-Type": "application/json",
						Authorization: "Bearer " + store.bearer_token
					}
				};
				await fetch(store.global_url + "api/get-budget", requestOptions_budget)
					.then(response => response.json())
					.then(data => setStore({budget: data}));
            },

            set_token_data: token =>{
                setStore({bearer_token: token})
            },

            update_local_budget_data: element =>{ //es un hotel, es un fotografo?? {name:hote,id:item.id}
                const store= getStore();

                if (element.category=="Flores"){
                    setStore({flower_indicator:element.id})
                    if (element.name){
                        setStore({flower_provider:element.name})
                    }else{
                        setStore({flower_provider:element.provider})
                    }
                }
                if (element.category=="Salon y comida"){
                    setStore({location_indicator:element.id})
                    if (element.name){
                        setStore({location_provider:element.name})
                    }else{
                        setStore({location_provider:element.provider})
                    }
                }
                if (element.category=="Fotografia"){
                    setStore({photo_indicator:element.id})
                    if (element.name){
                        setStore({photo_provider:element.name})
                    }else{
                        setStore({photo_provider:element.provider})
                    }
                }
            },

            budget_array_assignment: () => {
                const store = getStore();
                let temp_updated_budget_array=[0,0,0];

                if (store.flower_indicator){
                    temp_updated_budget_array[0]=parseInt(store.flower_indicator);
                }
                if (store.location_indicator){
                    temp_updated_budget_array[1]=parseInt(store.location_indicator);
                }
                if (store.photo_indicator){
                    temp_updated_budget_array[2]=parseInt(store.photo_indicator);
                }
                setStore({updated_budget_array:temp_updated_budget_array});
                console.log(store.updated_budget_array)
            },

			updateBudget: async updated_budget_array => {
                const store = getStore();
				const urlAPI = store.global_url + "api/update-budget";
				const updateOptions_budget = {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
						Authorization: "Bearer " + store.bearer_token
					},
					body: JSON.stringify([{service1_id:updated_budget_array[0],service2_id:updated_budget_array[1],service3_id:updated_budget_array[2]}])
				};

				const result = await fetch(urlAPI,updateOptions_budget)
					.then(res => res.json())
					.then(data => console.log(data));
				
			},

			get_services_data: async () => {
                const store = getStore();
				const urlAPI = store.global_url + "api/allserv";
				const get_services_data= {
					method: "GET",
					headers: {
						"Content-Type": "application/json"
					}
				};
				const result = await fetch(urlAPI,get_services_data)
					.then(res => res.json())
                    .then(data => setStore({services_data:data}));
                    
                console.log (store.services_data);

            },

            information_sorting_generator_flowers: () => {
                const store = getStore();
                console.log(store.services_data.flower);
                let flores_cr=[];
                let flores_gala=[];
                let flores_juno=[];
                let flores_nandallo=[];
                //flower sorting
                if (store.services_data.flower){
                    store.services_data.flower.map((item,index)=>{
                        
                        if(index<=2){
                            flores_cr.push(item);
                        }
                        if((index>2)&&(index<=5)){
                            flores_gala.push(item);
                        }
                        if((index>5)&&(index<=8)){
                            flores_juno.push(item);
                        }
                        if((index>8)&&(index<=11)){
                            flores_nandallo.push(item);
                        }
                        
                    });   
                        setStore({flores_cr_data:flores_cr});
                        setStore({flores_gala_data:flores_gala});
                        setStore({flores_juno_data:flores_juno});
                        setStore({flores_nandallo_data:flores_nandallo});
                        console.log(store.flores_cr_data)
                        console.log(store.flores_gala_data)
                        console.log(store.flores_juno_data)
                        console.log(store.flores_nandallo_data)
                }
            
            },
            
            information_sorting_generator_locations: () => {
                const store = getStore();
                let herradura=[];
                let sheraton=[];
                let papagayo=[];
                let swiss_travel=[];
                //flower sorting
                if (store.services_data.location){
                    store.services_data.location.map((item,index)=>{
                        
                        if(index<=2){
                            herradura.push(item);
                        }
                        if((index>2)&&(index<=5)){
                            sheraton.push(item);
                        }
                        if((index>5)&&(index<=8)){
                            papagayo.push(item);
                        }
                        if((index>8)&&(index<=11)){
                            swiss_travel.push(item);
                        }
                    });
                        setStore({herradura_data:herradura});
                        setStore({sheraton_data:sheraton});
                        setStore({papagayo_data:papagayo});
                        setStore({swiss_travel_data:swiss_travel});

                        console.log(store.herradura_data)
                        console.log(store.sheraton_data)
                        console.log(store.papagayo_data)
                        console.log(store.swiss_travel_data)
                    }
                    
                },
            
                information_sorting_generator_photo: () => {
                const store = getStore();
                let gabriel_anta=[];
                let douglas_cedeno=[];
                let raw_shoots=[];
                let geoff_photo=[];
                //flower sorting
                if (store.services_data.photo){
                    store.services_data.photo.map((item,index)=>{
                        if(index<=2){
                            gabriel_anta.push(item);
                        }
                        if((index>2)&&(index<=5)){
                            douglas_cedeno.push(item);
                        }
                        if((index>5)&&(index<=8)){
                            raw_shoots.push(item);
                        }
                        if((index>8)&&(index<=11)){
                            geoff_photo.push(item);
                        }
                    });
                        setStore({gabriel_anta_data:gabriel_anta});
                        setStore({douglas_cedeno_data:douglas_cedeno});
                        setStore({raw_shoots_data:raw_shoots});
                        setStore({geoff_photography_data:geoff_photo});

                        console.log(store.gabriel_anta_data)
                        console.log(store.douglas_cedeno_data)
                        console.log(store.raw_shoots_data)
                        console.log(store.geoff_photography_data)
                    }

            },
            getCurreciesInformations: async () => {
                    const store= getStore();
                    let api_info;
                    fetch('http://api.exchangeratesapi.io/v1/latest?access_key=4240e58268baa587b51dbc673750119d&symbols=USD,AUD,CAD,PLN,CRC')
                    .then(Response => Response.json()).then(data => {
                        console.log(data);
                        setStore({USD_api:data.rates.USD});
                        setStore({CRC_api:data.rates.CRC});
                        setStore({USDvsCRC:store.CRC_api/store.USD_api})
                        console.log(store.USDvsCRC);

                        
                    })
                    
            },
            email_recovery_function: async email =>{

                const store = getStore();
                let response_status;
				const urlAPI = store.global_url + "api/return-password";
				const get_user_data= {
					method: "POST",
					headers: {
						"Content-Type": "application/json"
					},
                    body: JSON.stringify({email:email})
				};
				const result = await fetch(urlAPI,get_user_data)
					.then(res => res.json())
                    .then(data => response_status=data);
                
                if (response_status=="email sent"){
                    setStore({recovery_redirect:true})
                    alert("Tu contraseña ha sido enviada a tu email!")
                }else{
                    alert("El correo que has insertado no esta relacionado con ninguna cuenta.")
                }

            }
            
            }

			}

    };
    

export default getState;
