package com.example.teeradej.cxrapp.models;

import javax.persistence.*;

@Entity
@Table(name = "roles")
public class Role {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;

	@Enumerated(EnumType.STRING)
	@Column(length = 20)
	private ERole name;

	public Role() {

	}

	public Role(ERole name) {
		this.name = name;
	}

	public Integer getId() {
		return this.id;
	}

	public ERole getName() {
		return this.name;
	}

	public void setName(ERole name) {
		this.name = name;
	}
}
