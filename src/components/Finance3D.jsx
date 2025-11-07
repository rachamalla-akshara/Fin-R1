import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Line } from '@react-three/drei';
import * as THREE from 'three';

function Graph() {
  const ref = useRef();
  const points = useMemo(() => {
    const arr = [];
    for (let i = 0; i < 200; i++) {
      const x = (i - 100) / 10;
      const y = Math.sin(i * 0.12) * 0.7 + Math.cos(i * 0.05) * 0.2 + (Math.random() - 0.5) * 0.15;
      arr.push(new THREE.Vector3(x, y, (i - 100) / 150));
    }
    return arr;
  }, []);

  useFrame(() => { if (ref.current) ref.current.rotation.y += 0.002; });

  return (
    <group ref={ref} position={[0, -0.2, 0]}>
      <Line points={points} color="#00ffd5" lineWidth={2} />
      {points.map((p, i) => (
        <mesh key={i} position={p}>
          <sphereGeometry args={[0.03, 8, 8]} />
          <meshStandardMaterial emissive="#06b6d4" color="#0ea5e9" />
        </mesh>
      ))}
    </group>
  );
}

export default function Finance3D() {
  return (
    <Canvas style={{ position: 'absolute', inset: 0 }} camera={{ position: [0, 1.4, 4], fov: 50 }}>
      <color attach="background" args={["#0b1220"]} />
      <ambientLight intensity={0.6} />
      <directionalLight position={[5, 5, 5]} />
      <Graph />
      <OrbitControls enablePan enableZoom enableRotate />
    </Canvas>
  );
}
