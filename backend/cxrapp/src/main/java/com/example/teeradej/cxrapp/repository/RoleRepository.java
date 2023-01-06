package com.example.teeradej.cxrapp.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

import com.example.teeradej.cxrapp.models.ERole;
import com.example.teeradej.cxrapp.models.Role;

public interface RoleRepository extends JpaRepository<Role, Integer> {
	Optional<Role> findByName(ERole name);
}
