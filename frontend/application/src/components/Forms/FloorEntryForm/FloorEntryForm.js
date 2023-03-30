import React from "react";
import "./FloorEntryForm.css"


function FloorEntryForm(){

    return (
        <section className="page--entry--form">
            <section className="box--entry--form">
                <div className="info--entry--form">
                    <h1 className="title--entry--form">
                        Data Lantai
                    </h1>
                    <p>
                        Masukkan detail data lantai menggunakan form di bawah ini.
                    </p>
                </div>

                <form className="entry--form">
                    <div className="form--group--entry">
                        <label className="label--form--entry">Nama Lantai</label>
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
                            <label className="label--form--entry">Gedung</label>
                            <select className="select--form--entry">
                                <option value={0}>IGS Mayor Ruslan</option>
                                <option value={1}>IGS Veteran</option>
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

                    <input className="submit--form--entry" type="submit" value="Registrasikan Lantai" />

                </form>


            </section>
        </section>
    );
}


export default FloorEntryForm;