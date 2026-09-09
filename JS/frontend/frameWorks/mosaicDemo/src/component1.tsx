

export default function Component1(){
    const content = ["component 1 text 1", "component 1 text 2", "component 1 text 3"]
    let display = content.map((el, index)=>{
        return (
            <p key={index}>{el}</p>
        )
    })
    return(
        <div>
            {display}
        </div>
    )
}