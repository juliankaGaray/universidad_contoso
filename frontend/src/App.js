import React, { useEffect, useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
    const [cursos, setCursos] = useState([]);
    const [curso, setCurso] = useState({ titulo: "", creditos: "", descripcion: "" });

    // Obtener la lista de cursos al cargar la página
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/cursos/")
            .then(response => {
                setCursos(response.data);
                console.log("📌 Cursos obtenidos:", response.data);
            })
            .catch(error => console.error("❌ Error al obtener los cursos:", error));
    }, []);

    // Manejar cambios en los inputs
    const handleChange = (e) => {
        setCurso({ ...curso, [e.target.name]: e.target.value });
        console.log("📌 Nuevo estado del curso:", { ...curso, [e.target.name]: e.target.value });
    };

    // Enviar el formulario a Django
    const handleSubmit = (e) => {
        e.preventDefault();

        console.log("📢 Enviando datos a Django:", curso);  // Verificar qué datos se envían

        axios.post("http://127.0.0.1:8000/api/cursos/", curso, {
            headers: { "Content-Type": "application/json" }
        })
        .then(response => {
            console.log("✅ Curso agregado con éxito:", response.data);
            setCursos([...cursos, response.data]);  // Agregar el curso a la lista
            setCurso({ titulo: "", creditos: "", descripcion: "" });  // Limpiar el formulario
        })
        .catch(error => {
            console.error("❌ Error al enviar los datos:", error.response ? error.response.data : error);
        });
    };

    return (
        <div className="container mt-4">
            <h1 className="text-center text-primary">Gestión de Cursos</h1>

            {/* Formulario para agregar cursos */}
            <form className="mb-4" onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label className="form-label">Título</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        name="titulo" 
                        value={curso.titulo} 
                        onChange={handleChange} 
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label className="form-label">Créditos</label>
                    <input 
                        type="number" 
                        className="form-control" 
                        name="creditos" 
                        value={curso.creditos} 
                        onChange={handleChange} 
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label className="form-label">Descripción</label>
                    <textarea 
                        className="form-control" 
                        name="descripcion" 
                        value={curso.descripcion} 
                        onChange={handleChange} 
                        required 
                    ></textarea>
                </div>
                <button type="submit" className="btn btn-success w-100">Agregar Curso</button>
            </form>

            {/* Lista de Cursos */}
            <h2 className="text-center">Lista de Cursos</h2>
            <table className="table table-striped">
                <thead className="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Título</th>
                        <th>Créditos</th>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    {cursos.length > 0 ? (
                        cursos.map((c) => (
                            <tr key={c.id}>
                                <td>{c.id}</td>
                                <td>{c.titulo}</td>
                                <td>{c.creditos}</td>
                                <td>{c.descripcion}</td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="4" className="text-center">No hay cursos disponibles</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default App;
