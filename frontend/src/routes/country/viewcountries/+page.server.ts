/** @type {import('./$types').PageLoad} */
export const load = async () =>{
    const response = await fetch('http://127.0.0.1:8000/countries/')
    const countries =  response.json()
    return {countries}
}