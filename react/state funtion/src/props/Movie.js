let Movie=()=>{
    let movie_name="girl friend"
    let actresses="reshmika"
    let image="https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/the-girlfriend-et00423419-1733756512.jpg"
    return <div>
        <h2>movie:{movie_name}</h2>
        <h2>actress:{actresses}</h2>
        <img src={image} alt="" />

    </div>
}
export default Movie;