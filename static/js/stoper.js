function star(){
    
    let {PythonShell} = require('python-shell');
    let path = require('path');
    let options = {
        scriptPath: path.join(__dirname, '/controller'),
        pythonPath: '/usr/bin/python3'
    }

    PythonShell.run('main.py', options, function(err, results){
        if (err) throw err;
        console.log('results: %j', results);
    })
}