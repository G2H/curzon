/*

*/
function createDiv(div_class){
// create a div and assign a class
    a = document.createElement('div');
    a.className = div_class;
    return a;
}

function createLink(href){
// create a link and fill the href
    a = document.createElement('a');
    a['href'] = href;
    return a;
}

function updateText(id,new_text){
// update id's text
    document.getElementById(id).innerHTML = new_text;
}

function updateTitles(object){
    updateText('title_text',object.title);
    document.title = object.title;
   // updateText('subtitle_text',object.subtitle);
}

function createRow(object){
// given an object with link, title and subtitle element, return a row div
    var a = createLink(ifaNull(object.link));
    var onclick = document.createAttribute('onclick');
    onclick.value = 'changeId('+object.link_id+')';
    a.setAttributeNode(onclick);

    var line = createDiv('line');

    var row = document.createElement('row');
    var column = document.createElement('column');
    var cols = document.createAttribute('cols');
    cols.value = '12';
    column.setAttributeNode(cols);

    var icon = createDiv('icon');
    icon_unicode = document.createTextNode(ifNull(object.icon));
    icon.appendChild(icon_unicode);

    var line_title = createDiv('line_title');
    title = document.createTextNode(ifNull(object.title.slice(0,23)));
    line_title.appendChild(title);

    var line_subtitle = createDiv('line_subtitle');
    subtitle = document.createTextNode(ifNull(object.subtitle.slice(0,30)));
    line_subtitle.appendChild(subtitle);

    var chevron = createDiv('chevron');
    chevron_text = document.createTextNode('\u232A');
    chevron.appendChild(chevron_text);

    column.appendChild(icon);
    column.appendChild(line_title);
    column.appendChild(line_subtitle);
    column.appendChild(chevron);

    row.appendChild(column);
    line.appendChild(row);
    a.appendChild(line);

    return a;
}

function appendToDiv(id, element){
// appends an dom object to a div
    div = document.getElementById(id);
    div.appendChild(element)
}

var generateRows = function(rows){
// given an rows object, append them to the content div
    rows.forEach(function(row){
        var new_row = createRow(row);
        appendToDiv('content',new_row);
    })
}
function generatePage(object){
//given some html, appends it in the content div
    text_content = document.createElement('div');
    text_content.id = 'text_content';
    text_content.innerHTML = object;
    appendToDiv('content',text_content);
}

function createFooter(){
    //given an array, create X links and append them to the footer
}


function ifNull(element){
    if (typeof element !== 'undefined'){
        return element;
    }
    else {return '';}
}
function ifaNull(element){
    if (typeof element !== 'undefined'){
        return element;
    }
    else {return '#';}
}

function filterObject(object, column, value){
// given an object, a column and a value, filter that object
    return object.filter(function(d){return d[column] == value;});
}

function drawReturnButton(){
// draw return button with a link to previous page
    // delete the return button
    if (document.contains(document.getElementById("return_a"))) {
                document.getElementById("return_a").remove();
    }

    if(current_id != 1){
        var a = createLink('#');
        a.id = 'return_a'

        var onclick = document.createAttribute('onclick');
        onclick.value = 'changeId('+previous_ids[previous_ids.length - 1]+')';
        a.setAttributeNode(onclick);

        div = document.createElement('div');
        div.id = 'return_button';
        div_text = document.createTextNode('➔');

        div.appendChild(div_text);
        a.appendChild(div);

        document.getElementById('title').insertBefore(a, document.getElementById('title_text'));
    }
}

function renderPage(object,id){
    document.getElementById('content').innerHTML = '';
    updateTitles(object);
    var ObjectToRender = filterObject(object.pages,'id',id)[0];
    if(ObjectToRender.type=='menu'){generateRows(ObjectToRender.elements);}
    if(ObjectToRender.type=='page'){generatePage(ObjectToRender.elements);}
    drawReturnButton();
}

function changeId(newid){
    if (typeof current_id !== 'undefined' & typeof newid !== 'undefined') {
        newid !== previous_ids[previous_ids.length -1] && previous_ids.push(current_id); //only append if not return
        previous_ids.includes(newid) && previous_ids.pop(); 
        current_id = newid;
    }
    renderPage(data,current_id);
}