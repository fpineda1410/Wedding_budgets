import React, {useContext,useState} from 'react'
import { Col,Form, Input, Button, Cascader, Select, Row, Checkbox, AutoComplete  } from 'antd';
const { Option } = Select;

import { enquireScreen } from 'enquire-js';
import QueueAnim from 'rc-queue-anim';
import { Redirect } from "react-router-dom"; 

import { Context } from "../../store/appContext.js";



let isMobile;
enquireScreen((isMoving) => {
  isMobile = isMoving;
});


  const formItemLayout = {
    labelCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 8,
      },
    },
    wrapperCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 16,
      },
    },
  };
  const tailFormItemLayout = {
    wrapperCol: {
      xs: {
        span: 24,
        offset: 0,
      },
      sm: {
        span: 16,
        offset: 8,
      },
    },
  };

export const RecoveryForm =()=>  {

    const [form] = Form.useForm();

    const { store, actions } = useContext(Context);

    const [recovery_redirect, setRecoveryRedirect] = useState(false);

    
    const onFinish = (values) => {
        console.log(values); 
        actions.email_recovery_function(values.email);
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
           <strong>Wedding Budgets</strong> Recuperación de contraseña:
          </h1>

    <Form
      {...formItemLayout}
      form={form}
      name="register"
      onFinish={onFinish}
      
      scrollToFirstError
    >
                <Form.Item
                    name="email"
                    label="E-mail"
                    rules={[
                    {
                        type: 'email',
                        message: 'El Email no tiene un formato valido!',
                    }
                    ]}
                >
                    <Input />
                    
                </Form.Item>

                <Button type="primary" htmlType="submit">
                    Recuperar contraseña
                </Button>

        </Form>

        {store.recovery_redirect?
        <Redirect to="/"/>:''}

        </QueueAnim>
        
    )
}

