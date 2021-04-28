import React, { useContext, useState,useEffect } from 'react';
import { Modal, Button } from 'antd';


import { Context } from "../../../store/appContext.js";

function Info_form () {

  const [visible, setVisible] = useState(true);
  
  const { store, actions } = useContext(Context);
   
  return (
    <>
      <Modal
        title="Información de contacto:"
        centered
        visible={visible}
        onOk={() => setVisible(false)}
        onCancel={() => setVisible(false)}
        width={1000}
      >
        
        <p>Numero Telefonico<strong>6402 5410</strong></p>
        <p>Facebook<strong> <a href="https://www.facebook.com/Wedding-Budget-CR-101186272130279">Click aqui!</a></strong></p>
        <p>Instagram<strong><a href="https://www.instagram.com/weddingbudgetcr/?hl=es-la">Click aqui!</a></strong></p>
        
      </Modal>
    </>
  );
};

export default Info_form;