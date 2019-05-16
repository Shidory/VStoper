function activateStopper(){
    
    PythonShell = require('python-shell');
    path = require('path');
    
    var options = {
        scriptPath: path.join(__dirname, '/'),
        pythonPath: 'usr/bin/python3'
    }

    PythonShell.PythonShell.run('main.py', options, function(err, results){
        if (err) throw err;
        console.log('results: %j', results);
    });

}