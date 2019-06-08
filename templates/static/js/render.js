
var camera, scene, renderer;
var geometry, material, cloudPoints;

var mouse = new THREE.Vector2();

function animate() {
    requestAnimationFrame( animate );
    cloudPoints.rotation.y += 0.1 * Math.PI/180;
    control.update();
    renderer.render( scene, camera );
}


function ThreeInit(points, view=null) {
    // SCENE
    scene = new THREE.Scene();

    // CAMERA
    camera = new THREE.PerspectiveCamera(50, 4 / 3, .5, 1000);
    if(view){
        camera.position.set(view[0], view[1], view[2]);
    }
    else{
        camera.position.set(1,1,1);
    }
    camera.lookAt(0, -1, 0);
    
    // GEOMETRY
    geometry = new THREE.BufferGeometry();
    const numPoints = points.length;
    var positions = new Float32Array( numPoints * 3 );
    var colors = new Float32Array( numPoints * 3 );
    const baseColor = new THREE.Color( 0, 1, 1 );
    for(let i = 0; i < numPoints; i++){
        positions[i*3] = points[i][0];
        positions[i*3 + 1] = points[i][1];
        positions[i*3 + 2] = points[i][2];
        colors[i*3] = baseColor.r;
        colors[i*3 + 1] = baseColor.g;
        colors[i*3 + 2] = baseColor.b;
    }
    
    geometry.addAttribute( 'position', new THREE.BufferAttribute( positions, 3 ) );
    geometry.addAttribute( 'color', new THREE.BufferAttribute( colors, 3 ) );
    geometry.computeBoundingBox();
    const pointSize = 0.01;
    let material = new THREE.PointsMaterial( { size: pointSize, vertexColors: THREE.VertexColors } );
    cloudPoints = new THREE.Points(geometry, material);
    scene.add(cloudPoints);
    
    // RENDER
    renderer = new THREE.WebGLRenderer();
    let el = document.getElementById('3d-points');
    const width = el.offsetWidth;
    renderer.setSize(width, width*0.75);
    el.appendChild(renderer.domElement);
    window.addEventListener( 'resize', onWindowResize, false );
    // controls
    control = new THREE.TrackballControls(camera, el);
    animate();
}

function onDocumentMouseMove( event ) {
    event.preventDefault();
    mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
    mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
}
function onWindowResize() {
    let el = document.getElementById('3d-points');
    const width = el.offsetWidth;
    camera.aspect = 0.75;
    camera.updateProjectionMatrix();
    renderer.setSize(width, width*0.75);
}

