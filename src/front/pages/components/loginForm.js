import React from 'react'
import { Row, Col,Form, Input, Button, Checkbox  } from 'antd';
import { enquireScreen } from 'enquire-js';
import QueueAnim from 'rc-queue-anim';

let isMobile;

enquireScreen((b) => {
  isMobile = b;
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

    const onFinish = (values) => {
        console.log('Success:', values);
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

                <Form.Item {...tailLayout} name="remember" valuePropName="checked">
                    <Checkbox>Remember me</Checkbox>
                </Form.Item>

                <Form.Item {...tailLayout}>
                    <Button type="primary" htmlType="submit">
                    Submit
                    </Button>
                </Form.Item>
        </Form>
        </QueueAnim>
        
        
             
        
        
    )
}

