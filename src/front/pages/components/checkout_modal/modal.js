import React, { useContext, useState,useEffect } from 'react';
import { Modal, Button } from 'antd';


import { Context } from "../../../store/appContext.js";

function Checkout_form ({service_1_id,service_2_id,service_3_id}) {

  const [visible, setVisible] = useState(true);
  const [service1, setService1] = useState('');
  const [service2, setService2] = useState('');
  const [service3, setService3] = useState('');

  const { store, actions } = useContext(Context);
    let service1_array;
    let service2_array;
    let service3_array;
    
    service1_array=store.services_data.flower;
    service2_array=store.services_data.location;
    service3_array=store.services_data.photo;
    const service1_price = service_1_id ? parseInt(service1_array[service_1_id-1].price):0
    const service2_price=  service_2_id ? parseInt(service2_array[service_2_id-1].price):0
    const service3_price= service_3_id ? parseInt(service3_array[service_3_id-1].price):0

  return (
    <>
      <Modal
        title="Confirmar Presupuesto"
        centered
        visible={visible}
        onOk={() => setVisible(false)}
        onCancel={() => setVisible(false)}
        width={1000}
      >
        {service_1_id?<p>{service1_array[service_1_id-1].provider}......Precio<strong> $ {service1_array[service_1_id-1].price}</strong></p>:''}
        {service_2_id?<p>{service2_array[service_2_id-1].provider}......Precio<strong> $ {service2_array[service_2_id-1].price}</strong></p>:''}
        {service_3_id?<p>{service3_array[service_3_id-1].provider}......Precio<strong> $ {service3_array[service_3_id-1].price}</strong></p>:''}
        <p>El total de su presupuesto sería de: Precio<strong> ${service1_price+service2_price+service3_price}</strong></p>
        
      </Modal>
    </>
  );
};

export default Checkout_form;