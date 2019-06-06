
var camera, scene, renderer;
var geometry, material, mesh;

function animate() {
    requestAnimationFrame( animate );
    mesh.rotation.x += 0.01;
    mesh.rotation.y += 0.02;
    renderer.render( scene, camera );
}


function ThreeInit(points) {
    // SCENE
    scene = new THREE.Scene();

    // CAMERA
    camera = new THREE.PerspectiveCamera(50, 4 / 3, .5, 1000);
    camera.position.set(3, 2, 1);
    camera.lookAt(0, 0, 0);
    
    // GEOMETRY
    geometry = new THREE.Geometry();
    
    geometry.vertices = points.map(([x,y,z])=>{
        return new THREE.Vector3(x,y,z);
    });
    for(let i =0; i<points.length-3;i+=2){
        geometry.faces.push(new THREE.Face3(i,i+1,i+2));
        geometry.faces.push(new THREE.Face3(i+1,i+2,i+3));
    }
    
    // compute Normals
    geometry.computeVertexNormals();
    
    // normalize the geometry
    geometry.normalize();
    
    // MESH with GEOMETRY, and Normal MATERIAL
    scene.add(new THREE.Mesh(
    
            // geometry as first argument
            geometry,
    
            // then Material
            new THREE.MeshNormalMaterial({
                side: THREE.DoubleSide
            })));
    
    // RENDER
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(320, 240);
    document.getElementById('3d-points').appendChild(renderer.domElement);
    renderer.render(scene, camera);
    // camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 0.01, 10 );
    // camera.position.z = 1;
    // scene = new THREE.Scene();
    // // GEOMETRY
    // var geometry = new THREE.Geometry();
 
    // // create an array of vertices by way of
    // // and array of vector3 instances
    // geometry.vertices.push(
 
    //     new THREE.Vector3(0, 0, 0),
    //     new THREE.Vector3(1, 0, 0),
    //     new THREE.Vector3(1, 1, 0),
    //     new THREE.Vector3(0, 1, 0),
 
    //     new THREE.Vector3(0, 0, -1),
    //     new THREE.Vector3(1, 0, -1),
    //     new THREE.Vector3(1, 1, -1),
    //     new THREE.Vector3(0, 1, -1));
 
    // // create faces by way of an array of
    // // face3 instances. (you just play connect
    // // the dots with index values from the
    // // vertices array)
    // geometry.faces.push(
 
    //     new THREE.Face3(0, 1, 2),
    //     new THREE.Face3(3, 0, 2),
    //     new THREE.Face3(4, 5, 6),
    //     new THREE.Face3(7, 4, 6),
 
    //     new THREE.Face3(0, 4, 1),
    //     new THREE.Face3(1, 4, 5),
    //     new THREE.Face3(3, 7, 2),
    //     new THREE.Face3(2, 7, 6));
 
    // // compute Normals
    // geometry.computeVertexNormals();
 
    // // normalize the geometry
    // geometry.normalize();
    // // geometry.vertices = points.map(([x,y,z])=>{
    // //     return new THREE.Vector3(x,y,z);
    // // });
    // // for(let i =0; i<points.length-1;i+=3){
    // //     geometry.faces.push(new THREE.Face3(i,i+1,i+2));
    // // }
    // material = new THREE.MeshNormalMaterial();
    
    // mesh = new THREE.Mesh( geometry, material );
    // scene.add( mesh );

    // renderer = new THREE.WebGLRenderer( { antialias: true } );
    // let el = document.getElementById('3d-points');
    // renderer.setSize( 400, 400 );
    // el.appendChild( renderer.domElement );
    // animate();
}

