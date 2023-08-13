function STLViewerEnable(classname) {
    var models = document.getElementsByClassName(classname);
    for (var i = 0; i < models.length; i++) {
        STLViewer(models[i], models[i].getAttribute("data-src"));
    }
}

function STLViewer(elem, model) {

    if (!WEBGL.isWebGLAvailable()) {
        elem.appendChild(WEBGL.getWebGLErrorMessage());
        return;
    }

    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    var camera = new THREE.PerspectiveCamera(
        80, // fov
        elem.clientWidth / elem.clientHeight, // aspect ratio
        1, // near
        1000 // far
    );
    renderer.setSize(elem.clientWidth, elem.clientHeight);
    elem.appendChild(renderer.domElement);

    window.addEventListener('resize', function () {
        renderer.setSize(elem.clientWidth, elem.clientHeight);
        camera.aspect = elem.clientWidth / elem.clientHeight;

        camera.position.set(30, 0, 0);
        //var box = getBox(1, 1, 1);

        //scene.add(box);

        camera.updateProjectionMatrix();
    }, false);

    var controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.rotateSpeed = 0.05;
    controls.dampingFactor = 0.1;
    controls.enableZoom = false;
    controls.enablePan = false;
    controls.autoRotate = true;
    controls.autoRotateSpeed = .30;

    var scene = new THREE.Scene();

    scene.add(new THREE.HemisphereLight(0xffffff, 0x080820, 1.5));

    (new THREE.STLLoader()).load(model, function (geometry) {
        var material = new THREE.MeshPhongMaterial({
            color: 0x00ff37,
            specular: 100,
            shininess: 100
        });
        var mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh)
        //const wireframe = new THREE.WireframeGeometry(mesh.geometry);
        const wireframe = new THREE.EdgesGeometry( mesh.geometry );
        scene.add(wireframe)
        
        // Compute the middle
        var middle = new THREE.Vector3();
        geometry.center();
        geometry.boundingBox.getCenter(middle);

        // rotate it
        mesh.rotateX(3 * Math.PI / 2) // 3pi/2

        // Center it
        mesh.position.x = -1 * middle.x;
        mesh.position.y = -1 * middle.y;
        mesh.position.z = -1 * middle.z;

        // Pull the camera away as needed
        var largestDimension = Math.max(geometry.boundingBox.max.x,
            geometry.boundingBox.max.y, geometry.boundingBox.max.z)
        camera.position.z = largestDimension * 1.6;
        
        // adjust FOV to ensure it does not scale strangly when resizing the window
        //camera.fov = 2 * Math.atan( geometry.height / ( 2 * cameraPosition.z ) ) * ( 180 / Math.PI );
        
        // move the camera to its desired starting position
        camera.position.y = largestDimension * 0.75
        camera.updateProjectionMatrix();


        var animate = function () {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }; animate();

    });
}