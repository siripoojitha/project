points = points.map(([x,y,z])=>{ 
    return new THREE.Vector3( x, z, y ); 
});
var camera, scene, renderer;
var geometry, material, mesh;

init();
animate();

function init() {
    camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 0.01, 10 );
    camera.position.z = 1;
    scene = new THREE.Scene();
    // var geometry = new THREE.ConvexGeometry( points );
    var geometry = new THREE.Geometry();
    geometry.vertices = points;
    material = new THREE.MeshNormalMaterial();

    mesh = new THREE.Mesh( geometry, material );
    scene.add( mesh );

    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.getElementById('3d-points').appendChild( renderer.domElement );

}

function animate() {
    requestAnimationFrame( animate );
    mesh.rotation.x += 0.01;
    mesh.rotation.y += 0.02;
    renderer.render( scene, camera );
}