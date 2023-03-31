import React from "react";

import "../Forms.css"
import "./LocationEntryForm.css"


function LocationEntryForm(){

    return (
        <section className="page--entry--form">
            <section className="box--entry--form">
                <div className="info--entry--form">
                    <h1 className="title--entry--form">
                        Data Lokasi / Ruang
                    </h1>
                    <p>
                        Masukkan detail data lokasi atau ruangan menggunakan form di bawah ini.
                    </p>
                </div>

                <form className="entry--form">
                    <div className="form--group--entry">
                        <label className="label--form--entry">Nama Lokasi / Ruang</label>
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

                    <div className="entry--form">
                        <div className="form--group--entry">
                            <label className="label--form--entry">Lantai</label>
                            <select className="select--form--entry">
                                <option value={0}>Lantai GF</option>
                                <option value={1}>Lantai MZ</option>
                                <option value={2}>Lantai L1</option>
                            </select>

                            <div></div>
                            <div className="error">
                                <small>
                                    Error
                                </small>
                            </div>
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

                    <div className="form--group--entry">
                        <label className="label--form--entry">Foto Lokasi</label>
                        <div className="upload--form--entry">
                            <div className="box--icon--building">
                                <box-icon className="icon--building" name="map" size="100pt" ></box-icon>
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

                    <input className="submit--form--entry" type="submit" value="Registrasikan Lokasi" />

                </form>


            </section>
        </section>
    );
}


export default LocationEntryForm;