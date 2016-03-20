/**
 * Created by meamka on 17.03.16.
 */


var addFileBtn = document.getElementById('add-file-btn');
var addFolderBtn = document.getElementById('add-folder-btn');
var metaBtns = document.getElementsByClassName('meta-btn');


function promptFilename(msg) {
    var res = prompt(msg + ':');
    if (res)
        console.log(res);
    else
        console.log('Nothing to do');

    return res;
}

window.addEventListener('load', function () {
    addFileBtn.addEventListener('click', function () {
        var filename = promptFilename('Enter file name');
        if (!filename)
            return false;

        window.location.href = '/add/file?name=' + filename
    });

    addFolderBtn.addEventListener('click', function () {
        var filename = promptFilename('Enter folder name');
        if (!filename)
            return false;

        window.location.href = '/add/folder?name=' + filename
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip();

        $('.meta-btn').on('click', function (event) {
            event.preventDefault();

            $('#meta-container').load(this.getAttribute('href') + ' #metadata', function () {
                $('.modal-title').text(this.getAttribute('data-file'));
                $('#metaModal').modal('show');
            });
        });
    });
});
