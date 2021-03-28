from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Not implemented. You probably meant to go to /FDP.'
    
@app.route('/FDP')
@app.route('/fdp')
def fdp():
    return render_template('./fdp.ttl.html')
    
    
@app.route('/FDP/catalog/phenotypic.ttl')
def catalog():
    return render_template('./catalog.ttl.html')
    
    
@app.route('/FDP/dataset/Dataset_1.ttl')
def dataset():
    return render_template('./dataset.ttl.html')
    
    
@app.route('/FDP/distribution/Pheno_dataset_1_sparql.ttl')
def distribution():
    return render_template('./distribution.ttl.html')
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=43131, debug=False)
