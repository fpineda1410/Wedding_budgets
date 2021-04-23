import React, {useContext,useState} from 'react'
import { Row, Col,Form, Input, Button, Checkbox  } from 'antd';
import { enquireScreen } from 'enquire-js';
import QueueAnim from 'rc-queue-anim';

import { Redirect } from "react-router-dom"; 

import { Context } from "../../store/appContext.js";

let isMobile;

enquireScreen((isMoving) => {
  isMobile = isMoving;
});



const layout = {
    labelCol: {
      span: 8,
    },
    wrapperCol: {
      span: 16,
    },
  };
  const tailLayout = {
    wrapperCol: {
      offset: 8,
      span: 16,
    },
  };

export const LoginForm =()=>  {

    const { store, actions } = useContext(Context);
    const [login_redirect, setLoginRedirect] = useState(false);

    async function login_user (username, password) {

        let temp_token;
        let login_status;
        let initial_favorites;
        console.log(username,password);
        
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username, password: password })
        };

        await fetch(store.global_url + "api/login", requestOptions)
                .then(response => response.json())
                .then(data =>  temp_token=data.access_token);
        
        console.log(temp_token);
        actions.set_token_data(temp_token);
        
        if (temp_token){
            console.log("el bicho")
            console.log(login_status)
            setLoginRedirect(true);
        };

        const requestOptions_budget = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + temp_token
            }
        };

        await fetch(store.global_url + "api/get-budget", requestOptions_budget)
            .then(response => response.json())
            .then(data => initial_favorites=data);

        console.log("Favorites are"+initial_favorites[0]);
    }

    const onFinish = (values) => {
        console.log(values);
        login_user(values.username,values.password); 
    }; 
    
    const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
    };

    const animType = {
        queue: isMobile ? 'bottom' : 'left',
        one: isMobile
          ? {
              scaleY: '+=0.3',
              opacity: 0,
              type: 'from',
              ease: 'easeOutQuad',
            }
          : {
              x: '+=30',
              opacity: 0,
              type: 'from',
              ease: 'easeOutQuad',
            },
      };

    return (
        
        <QueueAnim
        type={animType.queue}
        key="text"
        leaveReverse
        ease={['easeOutCubic', 'easeInCubic']}
        component={Col}
        style={{margin: "20vh"}}
        
      >
          <h1 key="h1" style={{color:"rgb(114, 114, 114)"}}>
           <strong>Wedding Budgets</strong> Log In:
          </h1>

          <Form
                {...layout}
                name="basic"
                initialValues={{
                    remember: true,
                }}
                
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
                >
                <Form.Item
                    label="Username"
                    name="username"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your username!',
                    },
                    ]}
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    label="Password"
                    name="password"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your password!',
                    },
                    ]}
                >
                    <Input.Password />
                </Form.Item>

                

                <Form.Item {...tailLayout}>
                    <Button type="primary" htmlType="submit">
                    LogIn
                    </Button>
                </Form.Item>
        </Form>

        {login_redirect?
        <Redirect to="/dashboard"/>:''}

        </QueueAnim>
        
    )
}

