import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

import "../Forms.css"
import "./BuildingEntryForm.css";


function BuildingEntryForm(){

    return (
        <section className="page--entry--form">
            <section className="box--entry--form">
                <div className="info--entry--form">
                    <h1 className="title--entry--form">
                        Data Gedung
                    </h1>
                    <p>
                        Masukkan detail data gedung menggunakan form di bawah ini.
                    </p>
                </div>
                <form className="entry--form">
                    <div className="form--group--entry">
                        <label className="label--form--entry">Nama Gedung</label>
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
                        <label className="label--form--entry">Alamat</label>
                        <input  className="input--form--entry"
                                name="address" 
                                type="text" 
                                />

                        <div></div>
                        <div className="error">
                            <small>
                                Error
                            </small>
                        </div>
                    </div>

                    <div className="form--group--entry">
                        <div></div>

                        <div className="form--group--lr--entry">
                            <div className="left--entry">
                                <label className="label--form--entry">Kelurahan</label>
                                <input  className="input--form--entry"
                                        name="kelurahan" 
                                        type="text" 
                                        />
                                
                                <div></div>
                                <div className="error">
                                    <small>
                                        Error
                                    </small>
                                </div>
                            </div>

                            <div className="right--entry">
                                <label className="label--form--entry">Kecamatan</label>
                                <input  className="input--form--entry"
                                        name="kecamatan" 
                                        type="text" 
                                        />
                                
                                <div></div>
                                <div className="error">
                                    <small>
                                        Error
                                    </small>
                                </div>
                            </div>
                            
                        </div>

                    </div>

                    <div className="form--group--entry">
                        <div></div>

                        <div className="form--group--lr--entry">
                            <div className="left--entry">

                                <label className="label--form--entry">Provinsi</label>
                                <input  className="input--form--entry"
                                        name="provinsi" 
                                        type="text" 
                                        />

                                <div></div>
                                <div className="error">
                                    <small>
                                        error
                                    </small>
                                </div>

                            </div>

                            <div className="right--entry">
                                <label className="label--form--entry">Kode Pos</label>
                                <input  className="input--form--entry"
                                        name="zipcode" 
                                        type="text" 
                                        />
                                
                                <div></div>
                                <div className="error">
                                    <small>
                                        error
                                    </small>
                                </div>
                            </div>

                        </div>
                    </div>


                    <div className="form--group--entry">
                        <label className="label--form--entry">Foto Gedung</label>
                        <div className="upload--form--entry">
                            <div className="box--icon--building">
                                <box-icon className="icon--building" name="buildings" size="100pt" ></box-icon>
                            </div>
                            <input  className="input--form--entry file--entry"
                                name="photo" 
                                type="file" 
                                />
                        </div>

                        <div></div>
                        <div className="error">
                            <small>
                              
                            </small>
                        </div>
                    </div>


                    <div className="form--group--entry">
                        <label className="label--form--entry">Deskripsi / Catatan</label>
                        {/* <input  className="input--form--entry"
                                name="description" 
                                type="text" 
                                />
                        
                        <div></div> */}

                        <textarea   className="textarea--form--entry"
                                    rows={5}
                                    name="description"
                                    
                                        ></textarea>
                        <div className="error">
                            <small>
                                
                            </small>
                        </div>
                    </div>

                    <input className="submit--form--entry" type="submit" value="Registrasikan Gedung" />

                </form>
            </section>
        </section>
    )

}

export default BuildingEntryForm;
