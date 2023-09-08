// Define your api urls here
const mainUrl = 'http://127.0.0.1:5000';

const getMemberUrl = `${mainUrl}/getMember`;
const getMemberLevelUrl = `${mainUrl}/getMemberLevel`;
const getUOMUrl = `${mainUrl}/getUOM`;
const getProductUrl = `${mainUrl}/getProduct`;
const getOrderUrl = `${mainUrl}/getOrder`;

const insertMemberUrl =`${mainUrl}/insertMember`;

const deleteMemberUrl =`${mainUrl}/deleteMember`;

const productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
const productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';

const orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// Function to hide the Element
function hideElement(elementID) {
    document.getElementById(elementID).style.display = 'none';
};

// Function to show the Element
function showElement(elementID) {
    document.getElementById(elementID).style.display = 'block';
};


// Defining async function to fetch response function, hide loader once loaded, update table HTML
async function fetchResponseToTableBody(fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, 
    columnListDisplay, deleteUrl, columnListDelete) {
    
    //show loader until a response is fetched
    showElement(loaderElementID)

    // Fetch response
    const response = await fetch(fetchUrl);
   
    // Storing data in form of JSON
    let data = await response.json();
    // console.log(data); 
    // console.log(typeof data) 

    //if response fetched, hide the loader
    if (response) {
        hideElement(loaderElementID);
    }

    //Initialize table HTML
    let tHeadHTML = '';
    let tBodyHTML = '';


    //for each row object, generate table body HTML
    data.forEach((object, i) => {

        // filter only object with keys defined in columnListDisplay to show in final table
       if (columnListDisplay && columnListDisplay.length > 0) {
            objectDisplay = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListDisplay.includes(key)))
       }

        //for 1st row object, generate table header HTML
        if (i === 0) {
            let th ="";
            Object.keys(objectDisplay).forEach(key => {
                th += `<th>${key}</th>`;
            });
            tHeadHTML = `
                ${th}
                <th>Action</th>
            `;
        }


        //Generate strings for table body HTML
        let dataAttrList = [];
        let valueList = [];
        Object.keys(objectDisplay).forEach(key => {

            dataAttr = `data-${key.replace('_','-')} = "${objectDisplay[key]}"`;
            dataAttrList.push(dataAttr);

            value = `<td>${objectDisplay[key]}</td>`;
            valueList.push(value);
        });
        trAttr = dataAttrList.join(' ');
        td = valueList.join('');

        
        // filter only object with keys defined in columnListAction to do update or delete
        if (columnListDelete && columnListDelete.length > 0) {
            objectDelete = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListDelete.includes(key)))
        }

        //for each key in object, create one line of <input> form
        let formInputList = [];
        Object.keys(objectDelete).forEach(key => {
            formInput = `<input type="hidden" id="${key}" name="${key}" value="${objectDelete[key]}"></input>`
            formInputList.push(formInput)
        });
        inputs = formInputList.join('');       


        //Finalizing tableHTML
        tBodyHTML += `
            <tr ${trAttr}>
                ${td}
                <td>
                    <form action="${deleteUrl}" method="post">
                        ${inputs}
                        <input type="submit" value="delete" onclick="return confirm('Are you sure to delete ?')">
                    </form>
                </td>
            </tr>
        `;

    });


    // Update table innerHTML
    document.getElementById(tableHeadElementID).innerHTML = tHeadHTML;
    document.getElementById(tableBodyElementID).innerHTML = tBodyHTML;
};



// Function to set insertHTML
function setInsertHTML(targetElementID, insertUrl, objectInsert) {

    let insertHTML = ''
    Object.keys(objectInsert).forEach(key => {
        insertHTML += `
            <label id="${key}" name="${key}">${key}: </label>
            <input type="${objectInsert[key]}" id="${key}" name="${key}" required><br>
        `
    });

    document.getElementById(`${targetElementID}`).innerHTML = `
        <form action="${insertUrl}" method="post">
            ${insertHTML}
            <br><input class="submit-insert" type="submit" value="submit" onclick="return confirm('Are you sure to add ?')">
        </form>
    `

    hideElement(targetElementID);

}
