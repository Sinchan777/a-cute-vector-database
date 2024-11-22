use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn cosine_similarity(vec1: Vec<f64>, vec2: Vec<f64>) -> PyResult<f64> {
    if vec1.len() != vec2.len() {
        return Err(pyo3::exceptions::PyValueError::new_err("Vectors must have the same length."));
    }
    let dot_product: f64 = vec1.iter().zip(vec2.iter()).map(|(a, b)| a * b).sum();
    let norm_a: f64 = vec1.iter().map(|x| x.powi(2)).sum::<f64>().sqrt();
    let norm_b: f64 = vec2.iter().map(|x| x.powi(2)).sum::<f64>().sqrt();

    Ok(dot_product / (norm_a * norm_b))
}

#[pymodule]
fn vector_ops(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cosine_similarity, m)?)?;
    Ok(())
}
