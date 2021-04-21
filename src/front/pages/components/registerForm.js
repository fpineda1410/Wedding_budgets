import React, {useContext} from 'react'
import { Row, Col,Form, Input, InputNumber, Button } from 'antd';
import { enquireScreen } from 'enquire-js';
import QueueAnim from 'rc-queue-anim';

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

  const validateMessages = {

    required: '${label} is required!',
    types: {
      email: '${label} is not a valid email!',
      number: '${label} is not a valid number!',
    },
    number: {
      range: '${label} must be between ${min} and ${max}',
    },
  };

export const RegisterForm =()=>  {

    const { store, actions } = useContext(Context);
    
    const onFinish = (values) => {
      let user=values.user;
      actions.register_user(user.username,user.password,user.email,values.user.name,values.user.last_name,values.user.phone); 
      console.log(values.user);
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
           <strong>Wedding Budgets</strong> Registro:
          </h1>

        <Form {...layout} name="nest-messages" onFinish={onFinish} validateMessages={validateMessages}>
            <Form.Item
                name={['user', 'name']}
                label="Nombre"
                rules={[
                {
                    required: true,
                },
                ]}
            >
                <Input />
            </Form.Item>
            <Form.Item
                name={['user','last_name']}
                label="Apellidos"
                rules={[
                {
                  required: true,
                },
                ]}
            >
                <Input />
            </Form.Item>

            <Form.Item name={['user','username']}label="Username" rules={[
                {
                  required: true,
                }
                ]}>
              <Input />
            </Form.Item>

            <Form.Item name={['user', 'email']} label="Email" rules={[{ type: 'email' }]}>
              <Input />
            </Form.Item>
            
            <Form.Item name={['user','phone']} label="Numero Móvil">
              <Input />
            </Form.Item>
            
            <Form.Item
                    label="Password"
                    name={['user', 'password']} 
                    rules={[
                    {
                        required: true,
                        message: 'Please input your password!',
                    },
                    ]}
                >
                    <Input.Password />
                </Form.Item>
            

            
            <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
                <Button type="primary" htmlType="submit">
                Registrarme!
                </Button>
            </Form.Item>
    </Form>

    </QueueAnim>
        
        
             
        
        
    )
}

