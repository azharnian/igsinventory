import React from "react";

import "../Forms.css"
import "./ItemTypeForm.css"

function ItemTypeForm(){
    return (
        <section className="page--entry--form">
            <section className="box--entry--form">
                <div className="info--entry--form">
                    <h1 className="title--entry--form">
                        Data Tipe Barang
                    </h1>
                    <p>
                        Masukkan tipe barang menggunakan form di bawah ini.
                    </p>
                </div>

                <form className="entry--form">
                    <div className="form--group--entry">
                        <label className="label--form--entry">Tipe Barang</label>
                        <input  className="input--form--entry"
                                name="name" 
                                type="text" 
                                autoFocus />
                        
                        <div></div>
                        <div className="error">
                            <small>
                                Error
                            </small>
                        </div>
                    </div>


                    <div className="form--group--entry">
                        <label className="label--form--entry">Deskripsi / Catatan</label>

                        <textarea   className="textarea--form--entry"
                                    rows={5}
                                    name="description"
                                    
                                        ></textarea>
                        <div className="error">
                            <small>
                                
                            </small>
                        </div>
                    </div>


                    <input className="submit--form--entry" type="submit" value="Registrasikan Tipe Barang" />

                </form>


            </section>
        </section>
    );
}

export default ItemTypeForm;